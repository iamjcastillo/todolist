from fastapi import FastAPI

from myapp.application.routers import todo_routers

app = FastAPI()

# Register the routers
app.include_router(todo_routers.router)
