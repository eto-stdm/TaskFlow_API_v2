from fastapi import APIRouter
from app.api.v1.endpoints import tasks, users, projects

router = APIRouter()

router.include_router(tasks.router)
router.include_router(projects.router)
router.include_router(users.router)