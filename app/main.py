from fastapi import FastAPI
from mangum import Mangum
from .routes import task_routes

app = FastAPI()
handler = Mangum(app)

app.include_router(task_routes.router)