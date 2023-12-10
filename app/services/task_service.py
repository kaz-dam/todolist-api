from uuid import uuid4

from ..models.api_response import ApiResponse
from ..models.task import Task
from ..config import dynamodb_client

class TaskService:

    def __init__(self):
        self.table = dynamodb_client.Table('todolist-api-dev')

    def get_tasks(self):
        response = self.table.scan()

        if response['ResponseMetadata']['HTTPStatusCode'] != 200:
            return ApiResponse(error=True, message="Failed to retrieve tasks", status_code=500)
        
        return ApiResponse(data=response['Items'], status_code=200, error=False)


    def get_task(self, task_id: str):
        response = self.table.get_item(Key={'id': task_id})

        if response['ResponseMetadata']['HTTPStatusCode'] != 200:
            return ApiResponse(error=True, message="Failed to retrieve task", status_code=500)
        
        return ApiResponse(data=response['Item'], status_code=200, error=False)


    def create_task(self, task: Task):

        task.id = str(uuid4())
        
        response = self.table.put_item(Item=task.model_dump())

        if response['ResponseMetadata']['HTTPStatusCode'] != 200:
            return ApiResponse(error=True, message="Failed to create task", status_code=500)

        return ApiResponse(error=False, data=task, status_code=201)
    
    @classmethod
    def get(cls):
        return cls()