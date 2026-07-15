from pydantic import BaseModel, field_validator

class Task(BaseModel):
    text: str
    is_done: bool = False

    @field_validator("text")
    def validate_text(cls, value):
        if len(value) > 100:
            raise ValueError(f"text должен быть меньше 100 символов. Текущее значение: {value}")
        return value