from fastapi import APIRouter

router = APIRouter()

@router.get("/tasks", summary="Get all tasks")
async def get_tasks():
    return {"tasks": []}