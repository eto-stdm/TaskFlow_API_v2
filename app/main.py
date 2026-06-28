from fastapi import FastAPI

from app.api.v1.router import router
from fastapi_pagination import add_pagination

app = FastAPI()
add_pagination(app)

app.include_router(router)

@app.get("/")
def root():
    """Корневая директория"""
    return {"message": "Приложение по управлению задачами 'TaskFlow API' v2"}