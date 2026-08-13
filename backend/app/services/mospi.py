import requests
import urllib3

from app.config import MOSPI_API_KEY, MOSPI_BASE_URL

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def list_datasets(page=1):

    response = requests.get(
        f"{MOSPI_BASE_URL}/api/listdatasets",
        headers={
            "X-API-KEY": MOSPI_API_KEY,
        },
        params={
            "page": page,
        },
        verify=False,
        timeout=30,
    )

    response.raise_for_status()

    return response.json()


def list_files(dataset_id):

    response = requests.get(
        f"{MOSPI_BASE_URL}/api/datasets/{dataset_id}/files",
        headers={
            "X-API-KEY": MOSPI_API_KEY,
        },
        verify=False,
        timeout=30,
    )

    print("=" * 60)
    print("Dataset ID :", dataset_id)
    print("Status     :", response.status_code)
    print(response.text)
    print("=" * 60)

    response.raise_for_status()

    return response.json()