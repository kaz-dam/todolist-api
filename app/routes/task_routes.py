from fastapi import APIRouter
from typing import List
from ..models.task import Task

router = APIRouter()

@router.get("/tasks", response_model=List[Task], summary="Get all tasks")
async def get_tasks():
    return []