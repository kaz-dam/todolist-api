import boto3
from boto3.dynamodb.conditions import Key
from fastapi import Request, Response

def get_dynamodb_client():
    return boto3.resource('dynamodb')

dynamodb_client = get_dynamodb_client()

async def add_security_headers(request: Request, call_next):
    response: Response = await call_next(request)
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["Content-Security-Policy"] = "default-source 'self'"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    return response