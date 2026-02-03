from fastapi import FastAPI
from pydantic import BaseModel

from tlacuilo.core.config import BUILTIN_TEMPLATES_DIR, USER_TEMPLATES_DIR
from tlacuilo.printer.print import render_and_execute_template
from tlacuilo.printer.setup import get_printer

app = FastAPI()


class TodoRequest(BaseModel):
    template: str = "todo.j2"
    todo: str


@app.post("/todo")
def create_todo(req: TodoRequest):
    printer = get_printer()
    render_and_execute_template(
        printer=printer,
        template_name=req.template,
        context={"todo": req.todo},
        user_templates_dir=USER_TEMPLATES_DIR,
        builtin_templates_dir=BUILTIN_TEMPLATES_DIR,
    )
    return {"ok": True}
