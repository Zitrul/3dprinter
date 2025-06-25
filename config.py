import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

PRINTERS = [
    {
        "name": "ANYCUBIC I3 MEGA",
        "baud": 250000,
        "port": "COM4",
        "status": "w"  # w - waiting, p - printing, o - offline
    }
]
