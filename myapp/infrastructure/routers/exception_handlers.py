from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

from myapp.domain.exceptions import TitleTooLongException, ToDoListNotFoundException


def register_exception_handlers(app: FastAPI):
    @app.exception_handler(TitleTooLongException)
    def title_too_long_exception_handler(_: Request, exc: TitleTooLongException):
        return JSONResponse(
            status_code=HTTP_400_BAD_REQUEST,
            content={"message": "Task title is too long. It should be under 50 characters long."}
        )

    @app.exception_handler(ToDoListNotFoundException)
    def to_do_list_not_found_exception_hadler(_: Request, exc: ToDoListNotFoundException):
        return JSONResponse(
            status_code=HTTP_404_NOT_FOUND,
            content={"message": "To do list not found."}
        )
