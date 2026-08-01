from fastapi import FastAPI

from app.routes.datasets import router as datasets_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="MoSPI API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:1313",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "MoSPI API Running"}


app.include_router(
    datasets_router,
    prefix="/api",
    tags=["Datasets"],
)