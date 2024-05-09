import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

test = os.getenv("DATABASE FILENAME")

try:
    load_dotenv()
except FileNotFoundError:
    pass

DATABASE_FILENAME = os.getenv("DATABASE FILENAME") or "database.sqlite"
print(DATABASE_FILENAME)
DATABASE_FILE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILENAME)
print(DATABASE_FILE_PATH)
