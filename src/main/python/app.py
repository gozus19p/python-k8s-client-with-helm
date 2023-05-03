from flask import Flask, jsonify, Response

import service.client as service

app = Flask(__name__)


@app.route("/api/v1/configmap/<configmap_name>", methods=["GET"])
def read_configmap(configmap_name: str) -> Response:
    return jsonify(service.read_configmap(configmap_name))


@app.route("/api/v1/secret/<secret_name>", methods=["GET"])
def read_secret(secret_name: str) -> Response:
    return jsonify(service.read_secret(secret_name))


if __name__ == "__main__":
    app.run(debug=True)
