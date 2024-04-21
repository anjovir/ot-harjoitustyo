import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv()
except FileNotFoundError:
    pass

DATABASE_FILENAME = os.getenv("DATABASE FILENAME") or "database.sqlite"
DATABASE_FILE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILENAME)
