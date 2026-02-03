import os
from pathlib import Path

CONNECTION_METHOD = os.getenv("CONNECTION_INTERFACE", "Network")

USER_TEMPLATES_DIR = Path("templates")
BUILTIN_TEMPLATES_DIR = Path("src/tlacuilo/templates/builtin")
