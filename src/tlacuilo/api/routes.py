import logging
import os

import uvicorn
from fastapi import Depends, FastAPI
from pydantic import BaseModel

from tlacuilo.api.auth import verify_key
from tlacuilo.core.config import BUILTIN_TEMPLATES_DIR, USER_TEMPLATES_DIR
from tlacuilo.core.log_config import LOGGING_CONFIG
from tlacuilo.printer.print import render_and_execute_template
from tlacuilo.printer.setup import get_printer

app = FastAPI()

log = logging.getLogger(__name__)


class TodoRequest(BaseModel):
    template: str = "todo.j2"
    todo: str


@app.post("/todo", dependencies=[Depends(verify_key)])
def create_todo(req: TodoRequest):
    log.info("Todo Received")
    printer = get_printer()
    render_and_execute_template(
        printer=printer,
        template_name=req.template,
        context={"todo": req.todo},
        user_templates_dir=USER_TEMPLATES_DIR,
        builtin_templates_dir=BUILTIN_TEMPLATES_DIR,
    )
    return {"ok": True}


def main() -> None:
    uvicorn.run(
        "tlacuilo.api.routes:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_config=LOGGING_CONFIG,
        log_level=os.getenv("LOG_LEVEL", "info").lower(),
        use_colors=True,
    )
