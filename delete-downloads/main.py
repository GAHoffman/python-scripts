import os
from dotenv import load_dotenv

load_dotenv()

FILE_PATH = os.getenv("FILE_PATH")

print(FILE_PATH)
