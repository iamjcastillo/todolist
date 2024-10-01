from fastapi import FastAPI

from myapp.infrastructure.routers import todo_routers

app = FastAPI()

app.include_router(todo_routers.router)
