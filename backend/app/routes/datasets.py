from fastapi import APIRouter

from app.services.mospi import list_datasets

router = APIRouter()


@router.get("/datasets")
def datasets(page: int = 1):
    return list_datasets(page)