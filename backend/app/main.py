from fastapi import FastAPI

from app.routes.datasets import router as datasets_router

app = FastAPI(title="MoSPI API")


@app.get("/")
def root():
    return {"message": "MoSPI API Running"}


app.include_router(
    datasets_router,
    prefix="/api",
    tags=["Datasets"],
)