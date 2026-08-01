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