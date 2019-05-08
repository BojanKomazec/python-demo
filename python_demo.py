import json
import os

from dotenv import load_dotenv
from src.util.debug import printDebugInfo


def main():
    printDebugInfo()
    load_dotenv(verbose=True)
    PYTHON_ENV = os.getenv("PYTHON_ENV")
    print("PYTHON_ENV =", PYTHON_ENV)
    config = json.load(open('config/config-'+PYTHON_ENV+'.json'))
    print("config =", config)

if __name__ == "__main__":
    main()
