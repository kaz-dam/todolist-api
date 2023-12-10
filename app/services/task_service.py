from uuid import uuid4

from ..models.api_response import ApiResponse
from ..models.task import Task
from ..config import dynamodb_client

def get_tasks():
    table = dynamodb_client.Table('todolist-api-dev')
    response = table.scan()

    if response['ResponseMetadata']['HTTPStatusCode'] != 200:
        return ApiResponse(error=True, message="Failed to retrieve tasks", status_code=500)
    
    return ApiResponse(data=response['Items'], status_code=200, error=False)


def get_task(task_id: str):
    table = dynamodb_client.Table('todolist-api-dev')
    response = table.get_item(Key={'id': task_id})

    if response['ResponseMetadata']['HTTPStatusCode'] != 200:
        return ApiResponse(error=True, message="Failed to retrieve task", status_code=500)
    
    return ApiResponse(data=response['Item'], status_code=200, error=False)


def create_task(task: Task):
    table = dynamodb_client.Table('todolist-api-dev')

    task.id = str(uuid4())
    
    response = table.put_item(Item=task.model_dump())

    if response['ResponseMetadata']['HTTPStatusCode'] != 200:
        return ApiResponse(error=True, message="Failed to create task", status_code=500)

    return ApiResponse(error=False, data=task, status_code=201)