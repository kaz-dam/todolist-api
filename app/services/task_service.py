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
        
        return response['Items']


    def get_task(self, task_id: str):
        response = self.table.get_item(Key={'id': task_id})

        if response['ResponseMetadata']['HTTPStatusCode'] != 200:
            return ApiResponse(error=True, message="Failed to retrieve task", status_code=500)
        
        if 'Item' not in response:
            return ApiResponse(error=True, message="Task not found", status_code=404)
        
        return response['Item']


    def create_task(self, task: Task):

        task.id = str(uuid4())
        
        response = self.table.put_item(Item=task.model_dump())

        if response['ResponseMetadata']['HTTPStatusCode'] != 200:
            return ApiResponse(error=True, message="Failed to create task", status_code=500)

        return task
    
    def update_task(self, task_id: str, task: Task):
        due_date = task.due_date.isoformat() if task.due_date else None
        response = self.table.update_item(
            Key={'id': task_id},
            UpdateExpression='SET title = :title, description = :description, due_date = :due_date, done = :done, #order = :order',
            ExpressionAttributeValues={
                ':title': task.title,
                ':description': task.description,
                ':due_date': due_date,
                ':done': task.done,
                ':order': task.order
            },
            ExpressionAttributeNames={
                '#order': 'order'
            },
            ReturnValues='UPDATED_NEW'
        )

        if response['ResponseMetadata']['HTTPStatusCode'] != 200:
            return ApiResponse(error=True, message="Failed to update task", status_code=500)

        return response['Attributes']
    
    def delete_task(self, task_id: str):
        response = self.table.delete_item(
            Key={'id': task_id},
            ReturnValues='ALL_OLD'
        )

        if response['ResponseMetadata']['HTTPStatusCode'] != 200:
            return ApiResponse(error=True, message="Failed to delete task", status_code=500)

        return response['Attributes']
    
    @classmethod
    def get(cls):
        return cls()