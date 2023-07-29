from flask import Flask, request, jsonify


def flask_process(port, match_id_queue):
    """Simple Flask application listening to GSI and sends match_ids detected to the Qt Application.

    Args:
        port: port to listen to
        match_id_queue: Queue to transmit the match_id
    """
    app = Flask(__name__)

    @app.route('/', methods=['POST'])
    def gsi_endpoint():
        payload = request.get_json()
        if 'map' in payload and "matchid" in payload["map"]:
            match_id = int(payload["map"]["matchid"])
            match_id_queue.put(match_id)
        return jsonify({})

    app.run(debug=False, port=port)
