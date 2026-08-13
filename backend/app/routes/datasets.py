from fastapi import APIRouter

from app.services.mospi import list_datasets, list_files

router = APIRouter(prefix="/api")


@router.get("/datasets")
def get_datasets(page: int = 1):
    return list_datasets(page)


@router.get("/datasets/{dataset_id}/files")
def get_dataset_files(dataset_id: int):
    return list_files(dataset_id)   