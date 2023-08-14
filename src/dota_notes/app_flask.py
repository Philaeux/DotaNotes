from flask import Flask, request, jsonify

from dota_notes.data.messages import MessageGSI


def flask_process(port, message_queue_qt):
    """Flask app spawner"""
    flask_app = FlaskApp(port, message_queue_qt)
    flask_app.run()


class FlaskApp:
    """Simple Flask application listening to GSI and sends info detected to the Qt Application.

    Args:
        port: port to listen to
        message_queue_qt: Queue to transmit the match information to the qt app
    """
    def __init__(self, port, message_queue_qt):
        self.app = Flask(__name__)
        self.port = port
        self.message_queue_qt = message_queue_qt
        self.last_match_id_sent = 0

        @self.app.route('/', methods=['POST'])
        def gsi_endpoint():
            payload = request.get_json()
            if 'map' in payload and "matchid" in payload["map"] and payload["map"]["matchid"] is not None:
                info = MessageGSI(int(payload["map"]["matchid"]))
                if self.last_match_id_sent == info.match_id or info.match_id == 0:
                    return jsonify({})

                self.last_match_id_sent = info.match_id
                self.message_queue_qt.put(info)
            return jsonify({})

    def run(self):
        self.app.run(debug=False, port=self.port)
