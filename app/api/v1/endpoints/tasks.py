from typing import TypeVar

from fastapi import APIRouter, HTTPException, Query
from fastapi_pagination import Page, paginate
from fastapi_pagination.customization import CustomizedPage, UseParamsFields

from app.test_data.tasks import tasks
from app.schemas.task import Task

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

T = TypeVar("T")

CustomPage = CustomizedPage[
    Page[T],
    UseParamsFields(
        size=Query(20, ge=1, le=100, alias="pageSize"),
        page=Query(1, ge=1, alias="pageNumber"),
    ),
]


@router.post("/", response_model=Task)
def create_task(task: Task):
    """Создание новой задачи"""
    tasks.append(task)
    return task


@router.get("/", response_model=CustomPage[Task])
def list_task(text_: str = None, is_done_: bool = None):
    """Вывод первых двадцати (по умолчанию) задач"""
    filtered = list()

    if text_ and is_done_ != None:
        for t in tasks:
            if text_.lower() in t["text"].lower() and is_done_ is t["is_done"]:
                filtered.append(t)
        return paginate(filtered)

    if text_:
        for t in tasks:
            if text_.lower() in t["text"].lower():
                filtered.append(t)
        return paginate(filtered)

    if is_done_ != None:
        for t in tasks:
            if is_done_ is t["is_done"]:
                filtered.append(t)
        return paginate(filtered)

    return paginate(tasks)


@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int) -> Task:
    """Вывод определённой задачи по индексу"""
    if task_id < len(tasks):
        return tasks.__getitem__(task_id)
    else:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")


@router.delete("/{task_id}", response_model=bool)
def delete_task(task_id: int) -> bool:
    """Удаление задачи по индексу"""
    if task_id < len(tasks):
        tasks.pop(task_id)
        return True
    else:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

@router.put("/{task_id}", response_model=Task)
def change_state_of_task(task_id: int) -> Task:
    """Изменение состояния задачи (завершена / не завершена)"""
    if task_id < len(tasks):
        tasks.__getitem__(task_id)["is_done"] = not tasks.__getitem__(task_id)["is_done"]
        return tasks.__getitem__(task_id)
    else:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")