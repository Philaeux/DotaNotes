from steam.client import SteamClient
from dota2.client import Dota2Client
from dota2.msg import EDOTAGCMsg

from dota_notes.data.messages.message_connect import MessageConnect, MessageDisconnect
from dota_notes.data.messages.message_connection_status import MessageConnectionStatus
from dota_notes.data.messages.message_server_id import MessageServerIdRequest, MessageServerIdResponse


def dota_process(match_id_in_queue, server_id_out_queue):
    """Dota client spawner"""
    app = DotaApp(match_id_in_queue, server_id_out_queue)
    app.run()


class DotaApp:
    """Dota client processing jobs requested by the Qt process.

    Attributes:
        user: Steam username
        password: Steam password
        message_queue_dota: Queue to receive jobs
        message_queue_qt: Queue to send job results
    """

    def __init__(self, message_queue_dota, message_queue_qt):
        self.user = ""
        self.password = ""
        self.message_queue_dota = message_queue_dota
        self.message_queue_qt = message_queue_qt
        self.message_buffer_queue = []

        self.steam = SteamClient()
        self.dota = Dota2Client(self.steam)
        self.dota_ready = False
        self.match_id = 0
        self.keep_running = True

        self.steam.on('logged_on', self.on_logged_on)
        self.dota.on('ready', self.on_dota_ready)
        self.steam.on('disconnected', self.on_disconnect)
        self.dota.on(EDOTAGCMsg.EMsgGCSpectateFriendGameResponse, self.on_spectate_response)

    def on_logged_on(self):
        self.message_queue_qt.put(MessageConnectionStatus("On", "Try"))
        self.dota.launch()

    def on_dota_ready(self):
        self.message_queue_qt.put(MessageConnectionStatus("On", "On"))
        self.dota_ready = True

    def on_disconnect(self):
        self.message_queue_qt.put(MessageConnectionStatus("Off", "Off"))

    def on_spectate_response(self, response):
        self.message_queue_qt.put(MessageServerIdResponse(response.server_steamid))

    def connect(self):
        self.message_queue_qt.put(MessageConnectionStatus("Try", "Off"))
        self.steam.login(username=self.user, password=self.password)

    def run(self):
        while self.keep_running:
            if self.dota_ready and len(self.message_buffer_queue) > 0:
                message = self.message_buffer_queue.pop(0)
                if isinstance(message, MessageServerIdRequest):
                    self.dota.send(EDOTAGCMsg.EMsgGCSpectateFriendGame, {'steam_id': message.steam_id})
            if not self.message_queue_dota.empty():
                message = self.message_queue_dota.get(block=False)
                if isinstance(message, MessageConnect):
                    self.user = message.user
                    self.password = message.password
                    self.connect()
                elif isinstance(message, MessageDisconnect):
                    self.steam.disconnect()
                else:
                    self.message_buffer_queue.append(message)
            self.steam.sleep(1)

    def stop(self):
        self.keep_running = False
