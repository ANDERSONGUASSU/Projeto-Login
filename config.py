import os
from dotenv import (
    load_dotenv,
)

load_dotenv()

DB_MENAGER = os.getenv("DB_MENAGER")
DB_USER = os.getenv("DB_USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
DB = os.getenv("DB")

DB_URL = f"{DB_MENAGER}://{DB_USER}:{PASSWORD}@{HOST}/{DB}"
