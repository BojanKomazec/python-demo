
# Use shebang to indicate which version of Python interpreter should be used
#!/usr/bin/env python3

import argparse
import json
import os

from dotenv import load_dotenv
from src.atexit_demo import atexit_demo
from src.chrome_extensions_demo import extract_extenson_id_demo
from src.class_demo import class_demo
from src.functions_demo import functions_demo
from src.glob_demo import glob_demo
from src.operators_demo import operators_demo
from src.os_demo import os_demo
from src.regular_expressions_demo import regular_expressions_demo
from src.subprocess_demo import subprocess_demo
from src.sys_demo import sys_demo
from src.threading_demo import threading_demo
from src.types_demo import types_demo
from src.util.debug import printDebugInfo
from src.variables_demo import variables_demo


def main():
    useCommandLineArgs = True
    # useCommandLineArgs = False

    if useCommandLineArgs:
        # construct the argument parse and parse the arguments
        ap = argparse.ArgumentParser()
        # ap.add_argument("-i", "--image", help = "path to the image file")
        # ap.add_argument("-c", "--coords", help = "comma seperated list of source points")
        ap.add_argument("--crx", dest="crx_file_path", help = "crx file path")
        cli_args = vars(ap.parse_args())
        # print(cli_args["image"])
        # print(cli_args["coords"])
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
        # operators_demo()
        # regular_expressions_demo()
        # types_demo()
        # python3 python_demo.py --crx="data/my_extension.crx"
        # extract_extenson_id_demo(cli_args["crx_file_path"])
    else:
        print("Not using command line arguments.\n")
        # functions_demo()
        # glob_demo()
        # regular_expressions_demo()
        # sys_demo()
        # subprocess_demo()
        # threading_demo()
        # types_demo()
        # atexit_demo()
        # variables_demo()

# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == "__main__":
    main()
