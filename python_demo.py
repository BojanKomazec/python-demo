import json
import os

from dotenv import load_dotenv
from src.util.debug import printDebugInfo
from src.class_demo import class_demo
from src.schema2db import schema2db


def main():
    printDebugInfo()
    # if .env does not exist, a warning is issued: UserWarning: File doesn't exist
    load_dotenv(verbose=True)
    # if .env does not exist, os.getenv will try to read system env variable
    PYTHON_ENV = os.getenv("PYTHON_ENV")
    print("PYTHON_ENV =", PYTHON_ENV)

    config = json.load(open('config/config-'+PYTHON_ENV+'.json'))
    print("config =", config)
    print("url =", config["url"])
    dir_name = config["dir"]

    # os.listdir() returns files in arbitrary order
    file_names = os.listdir(dir_name)
    file_names.sort()
    print("file_names =", file_names)
    for file_name in file_names:
        print("file name =", file_name)
        file_path = os.path.join(dir_name, file_name)
        print("file path =", file_path)
        print("file name without extension =", os.path.splitext(file_name)[0])
        print("file name without two last segments separated by '.' =", file_name.rsplit('.', 2)[0])

    class_demo()
    # schema2db()

if __name__ == "__main__":
    main()
