from fastapi import APIRouter, Depends

from ..models.api_response import ApiResponse
from ..models.task import Task
from ..services.task_service import TaskService


router = APIRouter()

@router.get("/tasks", response_model=ApiResponse, summary="Get all tasks")
async def get_tasks(task_service: TaskService = Depends(TaskService.get)):
    return task_service.get_tasks()


@router.post("/tasks", response_model=ApiResponse, summary="Create a new task")
async def create_task(task: Task, task_service: TaskService = Depends(TaskService.get)):
    return task_service.create_task(task)


@router.get("/tasks/{task_id}", response_model=ApiResponse, summary="Get a task by ID")
async def get_task(task_id: str, task_service: TaskService = Depends(TaskService.get)):
    return task_service.get_task(task_id)