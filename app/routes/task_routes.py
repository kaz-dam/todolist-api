from fastapi import APIRouter

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/", summary="Get all tasks")
async def get_tasks():
    return {"tasks": []}