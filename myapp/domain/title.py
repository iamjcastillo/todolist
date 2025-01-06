from pydantic import RootModel, field_validator

from myapp.domain.exceptions import TitleTooLongException

TITLE_MAX_LENGTH = 50


class Title(RootModel[str]):
    @field_validator("root", mode="before")
    def should_not_be_longer_than_50_characters(cls, value: str) -> str:
        if isinstance(value, str) and len(value) > TITLE_MAX_LENGTH:
            raise TitleTooLongException()
        return value
