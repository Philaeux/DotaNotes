from steam.client import SteamClient
from dota2.client import Dota2Client
from dota2.msg import EDOTAGCMsg

import logging
logging.basicConfig(format='[%(asctime)s] %(levelname)s %(name)s: %(message)s', level=logging.DEBUG)


def dota_process(username, password, match_id_in_queue, server_id_out_queue):
    app = DotaApp(username, password, match_id_in_queue, server_id_out_queue)
    app.run()


class DotaApp:
    def __init__(self, username, password, user_steam_id_in_queue, server_id_out_queue):
        self.username = username
        self.password = password
        self.user_steam_id_in_queue = user_steam_id_in_queue
        self.server_id_out_queue = server_id_out_queue

        self.steam = SteamClient()
        self.dota = Dota2Client(self.steam)
        self.dota_ready = False
        self.match_id = 0
        self.currentPage = 0
        self.keep_running = True

        self.steam.on('logged_on', self.start_dota)
        self.dota.on('ready', self.do_dota_stuff)
        self.dota.on('disconnected', self.on_disconnect)
        self.dota.on(EDOTAGCMsg.EMsgGCSpectateFriendGameResponse, self.on_spectate_response)

    def start_dota(self):
        self.dota.launch()

    def do_dota_stuff(self):
        self.dota_ready = True

    def on_disconnect(self):
        self.keep_running = False

    def on_spectate_response(self, response):
        self.server_id_out_queue.put(response.server_steamid)

    def run(self):
        self.steam.login(username=self.username, password=self.password)
        while self.keep_running:
            if self.dota_ready and not self.user_steam_id_in_queue.empty():
                user_steam_id = self.user_steam_id_in_queue.get(block=False)
                self.dota.send(EDOTAGCMsg.EMsgGCSpectateFriendGame, {'steam_id': int(user_steam_id)})
            self.steam.sleep(1)
