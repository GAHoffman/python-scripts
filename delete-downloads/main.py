import os
from dotenv import load_dotenv

load_dotenv()

# Separated into two separate env variables, one is for the specific folder path, and the other is for the file type to be deleted
folder_path = os.getenv("FOLDER_PATH")
print(folder_path)

file_type = os.getenv("FILE_TYPE")

# put both together in string format as the file_path
file_path = f"{folder_path}/{file_type}"
print(file_path)


if os.path.isfile(file_path):
    os.remove(file_path)
    print("File has successfully been deleted")
else:
    print("This file does NOT exist")
