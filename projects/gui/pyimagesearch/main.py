
# Use shebang to indicate which version of Python interpreter should be used
#!/usr/bin/env python3

import argparse
from pyimagesearch.transform import transform_example

def main():
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", help = "path to the image file")
    ap.add_argument("-c", "--coords", help = "comma seperated list of source points")
    cli_args = vars(ap.parse_args())
    print(cli_args["image"])
    print(cli_args["coords"])

    transform_example(cli_args)

if __name__ == "__main__":
    main()
