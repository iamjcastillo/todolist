from fastapi import FastAPI

from myapp.infrastructure.routers import todo_routers
from myapp.infrastructure.routers.exception_handlers import register_exception_handlers

app = FastAPI()

app.include_router(todo_routers.router)

register_exception_handlers(app)
