
# Use shebang to indicate which version of Python interpreter should be used
#!/usr/bin/env python3

import argparse
import json
import os

from dotenv import load_dotenv
from src.chrome_extensions_demo import extract_extenson_id_demo
from src.class_demo import class_demo
from src.functions_demo import functions_demo
from src.operators_demo import operators_demo
from src.os_demo import os_demo
from src.numpy_demo.demo import numpy_demo
from src.pandas_demo.demo import pandas_demo
from src.pyimagesearch.transform import transform_example
from src.regular_expressions_demo import regular_expressions_demo
from src.types_demo import types_demo
from src.util.debug import printDebugInfo

# To include this demo we need to list JSONSchema2DB in requirements.txt and also use Python < 3.8.
# This is because JSONSchema2DB requires psycopg2==2.7.2 (https://github.com/better/jsonschema2db/blob/master/setup.py)
# but this psycopg2 version does not support Python 3.8 as its support was added in psycopg 2.8.4.
# https://github.com/psycopg/psycopg2/issues/1106.
# from src.schema2db import schema2db

def main():
    # useCommandLineArgs = True
    useCommandLineArgs = False
    if useCommandLineArgs:
        # construct the argument parse and parse the arguments
        ap = argparse.ArgumentParser()
        ap.add_argument("-i", "--image", help = "path to the image file")
        ap.add_argument("-c", "--coords", help = "comma seperated list of source points")
        ap.add_argument("--crx", dest="crx_file_path", help = "crx file path")
        cli_args = vars(ap.parse_args())
        print(cli_args["image"])
        print(cli_args["coords"])
        print(f'crx_file_path = {cli_args["crx_file_path"]}')
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
        # transform_example(cli_args)
        # operators_demo()
        # regular_expressions_demo()
        # types_demo()

        # python3 python_demo.py --crx="data/my_extension.crx"
        # extract_extenson_id_demo(cli_args["crx_file_path"])
    else:
        # functions_demo()
        # regular_expressions_demo()
        # numpy_demo()
        # os_demo()
        # types_demo()
        pandas_demo()

# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == "__main__":
    main()
