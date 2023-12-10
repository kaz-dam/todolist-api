import boto3
from boto3.dynamodb.conditions import Key

def get_dynamodb_client():
    return boto3.resource('dynamodb')

dynamodb_client = get_dynamodb_client()