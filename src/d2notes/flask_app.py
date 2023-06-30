from flask import Flask, request, jsonify


def flask_process(match_id_queue):
    app = Flask(__name__)

    @app.route('/', methods=['POST'])
    def gsi_endpoint():
        payload = request.get_json()
        # print(payload)
        if 'map' in payload and "matchid" in payload["map"]:
            match_id = int(payload["map"]["matchid"])
            match_id_queue.put(match_id)
        return jsonify({})

    app.run(debug=False, port=58765)
