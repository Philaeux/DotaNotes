from steam.client import SteamClient
from dota2.client import Dota2Client
from steam.client.user import SteamUser
from dota2.msg import EDOTAGCMsg
from steam.enums.emsg import EMsg

import logging

logging.basicConfig(format='[%(asctime)s] %(levelname)s %(name)s: %(message)s', level=logging.DEBUG)


def steam_process(username, password, match_id_queue):
    app = SteamApp(username, password, match_id_queue)
    app.run()


class SteamApp:
    def __init__(self, username, password, match_id_queue):
        self.username = username
        self.password = password
        self.match_id_queue = match_id_queue

        self.steam = SteamClient()
        self.dota = Dota2Client(self.steam)
        self.dota_ready = False
        self.match_id = 0
        self.currentPage = 0

        @self.steam.on('logged_on')
        def start_dota():
            print("logged on")
            self.dota.launch()

        @self.dota.on('ready')
        def do_dota_stuff():
            self.dota_ready = True
            self.steam.request_persona_state(steam_ids=[76561197961298382])

        @self.dota.on('top_source_tv_games')
        def on_top_source_tv_games(response):
            self.game_list_index = response.game_list_index
            print("{} on page {}: {} games".format(self.game_list_index, self.currentPage, len(response.game_list)))
            games = []
            for game in response.game_list:
                games.append(game.match_id)
                if str(game.match_id) == str(self.match_id):
                    print(str(game))
            print(games)
            if len(games) != 10:
                print("end")
            else:
                self.currentPage += 1
                self.dota.request_top_source_tv_games(game_list_index=self.game_list_index, start_game=self.currentPage*10)

        @self.steam.on(EMsg.ClientPersonaState)
        def on_client_persona_state(message):
            print(message)
            print(message.friends)

    def run(self):
        self.steam.login(username=self.username, password=self.password)
        while True:
            if self.dota_ready and not self.match_id_queue.empty():
                self.match_id = self.match_id_queue.get(block=False)
                self.steam.request_persona_state(steam_ids=[76561197961298382])
                self.dota.request_top_source_tv_games()
            self.steam.sleep(10)
