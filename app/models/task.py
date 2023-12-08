from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    done: bool = False
    order: Optional[int] = None