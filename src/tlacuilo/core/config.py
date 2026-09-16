import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

LOG_LEVEL = os.getenv("LOG_LEVEL", "Info")

CONNECTION_METHOD = os.getenv("CONNECTION_METHOD", "Network")
PRINTER_IP = os.getenv("PRINTER_IP", "")
PRINTER_PORT = int(os.getenv("PRINTER_PORT", "9100"))

USER_TEMPLATES_DIR = Path("templates")
BUILTIN_TEMPLATES_DIR = Path("src/tlacuilo/templates/builtin")

API_KEY = os.getenv("API_KEY")
AUTH_ENABLED = os.getenv("AUTH_ENABLED")
