from steam.client import SteamClient
from dota2.client import Dota2Client
from dota2.msg import EDOTAGCMsg

import logging

from dota_notes.data.messages import Message, MessageType, MessageServerIdResponse, MessageConSatus, \
    MessageServerIdRequest

logging.basicConfig(format='[%(asctime)s] %(levelname)s %(name)s: %(message)s', level=logging.DEBUG)


def dota_process(username, password, match_id_in_queue, server_id_out_queue):
    app = DotaApp(username, password, match_id_in_queue, server_id_out_queue)
    app.run()


class DotaApp:
    def __init__(self, username, password, message_queue_dota, message_queue_qt):
        self.username = username
        self.password = password
        self.message_queue_dota = message_queue_dota
        self.message_queue_qt = message_queue_qt
        self.message_buffer_queue = []

        self.steam = SteamClient()
        self.dota = Dota2Client(self.steam)
        self.dota_ready = False
        self.match_id = 0
        self.keep_running = True

        self.steam.on('logged_on', self.on_logged_on)
        self.dota.on('ready', self.do_dota_stuff)
        self.dota.on('disconnected', self.on_disconnect)
        self.dota.on(EDOTAGCMsg.EMsgGCSpectateFriendGameResponse, self.on_spectate_response)

    def on_logged_on(self):
        self.message_queue_qt.put(Message(MessageType.CLIENTS_STATUS, MessageConSatus("On", "Try")))
        self.dota.launch()

    def do_dota_stuff(self):
        self.message_queue_qt.put(Message(MessageType.CLIENTS_STATUS, MessageConSatus("On", "On")))
        self.dota_ready = True

    def on_disconnect(self):
        self.message_queue_qt.put(Message(MessageType.CLIENTS_STATUS, MessageConSatus("Off", "Off")))

    def on_spectate_response(self, response):
        self.message_queue_qt.put(Message(MessageType.SERVER_ID_RESPONSE,
                                          MessageServerIdResponse(response.server_steamid)))

    def connect(self):
        self.message_queue_qt.put(Message(MessageType.CLIENTS_STATUS, MessageConSatus("Try", "Off")))
        self.steam.login(username=self.username, password=self.password)

    def run(self):
        while self.keep_running:
            if not self.message_queue_dota.empty():
                message = self.message_queue_dota.get(block=False)
                if message.message_type == MessageType.CLIENTS_CONNECT:
                    self.connect()
                else:
                    self.message_buffer_queue.append(message)
            if self.dota_ready and len(self.message_buffer_queue) > 0:
                message = self.message_buffer_queue.pop(0)
                if message.message_type == MessageType.SERVER_ID_REQUEST:
                    message_request: MessageServerIdRequest = message.payload
                    self.dota.send(EDOTAGCMsg.EMsgGCSpectateFriendGame, {'steam_id': int(message_request.account_id)})
            self.steam.sleep(1)

    def stop(self):
        self.keep_running = False
