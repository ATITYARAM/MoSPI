from dotenv import load_dotenv
import os

load_dotenv()

MOSPI_API_KEY = os.getenv("MOSPI_API_KEY")
MOSPI_BASE_URL = os.getenv("MOSPI_BASE_URL")