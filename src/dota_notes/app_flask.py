from flask import Flask, request, jsonify


def flask_process(port, match_info_queue):
    """Flask app spawner"""
    flask_app = FlaskApp(port, match_info_queue)
    flask_app.run()


class FlaskApp:
    """Simple Flask application listening to GSI and sends info detected to the Qt Application.

    Args:
        port: port to listen to
        match_info_queue: Queue to transmit the match information
    """
    def __init__(self, port, match_info_queue):
        self.app = Flask(__name__)
        self.port = port
        self.match_info_queue = match_info_queue
        self.last_match_id_sent = 0

        @self.app.route('/', methods=['POST'])
        def gsi_endpoint():
            payload = request.get_json()
            if ('map' in payload and "matchid" in payload["map"] and
                                     "player" in payload and
                                     "team2" in payload["player"] and
                                     len(payload["player"]["team2"]) > 1):
                info = {
                    "match_id": int(payload["map"]["matchid"]),
                    "players": []}
                if self.last_match_id_sent == info["match_id"] or info["match_id"] == 0:
                    return jsonify({})
                else:
                    self.last_match_id_sent = info["match_id"]

                for team in payload["player"].values():
                    for player in team.values():
                        if "accountid" not in player or "name" not in player:
                            continue
                        info["players"].append({"accountid": int(player["accountid"]), "name": player["name"]})

                self.match_info_queue.put(info)
            return jsonify({})

    def run(self):
        self.app.run(debug=False, port=self.port)
