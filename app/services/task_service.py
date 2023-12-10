from ..config import dynamodb_client

def get_tasks():
    table = dynamodb_client.Table('todolist-api-dev')
    response = table.scan()
    return response['Items']