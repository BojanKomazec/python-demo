import argparse
import json
import os

from dotenv import load_dotenv
from src.class_demo import class_demo
from src.functions_demo import functions_demo
from src.numpy_demo.demo import numpy_demo
from src.pyimagesearch.transform import transform_example
from src.schema2db import schema2db
from src.util.debug import printDebugInfo


def main():
    useCommandLineArgs = False
    if useCommandLineArgs:
        # construct the argument parse and parse the arguments
        ap = argparse.ArgumentParser()
        ap.add_argument("-i", "--image", help = "path to the image file")
        ap.add_argument("-c", "--coords", help = "comma seperated list of source points")
        cli_args = vars(ap.parse_args())
        print(cli_args["image"])
        print(cli_args["coords"])
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

        # class_demo()
        # schema2db()
        # numpy_demo()
        transform_example(cli_args)
    else:
        functions_demo()


if __name__ == "__main__":
    main()
