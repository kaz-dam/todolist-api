from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from os import getenv

from .config import add_security_headers
from .routes.task_routes import router as task_routes

app = FastAPI()
handler = Mangum(app)

app.include_router(task_routes)

# origins = [
#     "http://localhost:3000",
#     "https://todolist-frontend-kappa.vercel.app/"
# ]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"]
# )

# app.middleware(add_security_headers)

if getenv("ENV") == "production":
    app.docs_url = None
    app.redoc_url = None

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)