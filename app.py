
import os
import platform
import socket

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify({
        "service": "Docker Health API",
        "hostname": socket.gethostname(),
        "environment": os.getenv("APP_ENV", "development"),
        "python_version": platform.python_version()
    })


@app.get("/health")
def health():
    return jsonify({
        "status": "healthy"
    }), 200


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", "5001"))
    )
