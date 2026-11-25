
import os
import platform
import socket
import time

import psutil
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


@app.get("/system")
def system_health():

    # Actual CPU usage
    cpu_usage = psutil.cpu_percent(interval=5)

    # Actual memory information
    memory = psutil.virtual_memory()

    # Actual disk information
    disk = psutil.disk_usage("/")

    # System uptime
    uptime_seconds = int(time.time() - psutil.boot_time())

    return jsonify({
        "hostname": socket.gethostname(),

        "cpu": {
            "usage_percent": cpu_usage,
            "logical_cores": psutil.cpu_count()
        },

        "memory": {
            "total_mb": round(memory.total / (1024 ** 2), 2),
            "used_mb": round(memory.used / (1024 ** 2), 2),
            "available_mb": round(memory.available / (1024 ** 2), 2),
            "usage_percent": memory.percent
        },

        "disk": {
            "total_gb": round(disk.total / (1024 ** 3), 2),
            "used_gb": round(disk.used / (1024 ** 3), 2),
            "free_gb": round(disk.free / (1024 ** 3), 2),
            "usage_percent": disk.percent
        },

        "uptime_seconds": uptime_seconds
    }), 200


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", "5001"))
    )
