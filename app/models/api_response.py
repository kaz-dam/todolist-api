from pydantic import BaseModel
from typing import Generic, TypeVar, Optional, Any

DataT = TypeVar("DataT")

class ApiResponse(BaseModel, Generic[DataT]):
    data: Optional[DataT] = None
    message: Optional[str] = None
    error: bool = False
    status_code: int = 200