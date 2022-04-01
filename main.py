#! /usr/bin/env python

import os
import shutil
import sys
import argparse

# argparse stuff
def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        # %(prog)s
        usage="cgit [OPTION]",
        description="Add gitignore files"
    )

    parser.add_argument("-l", "--language", choices=["flutter", "csharp", "fsharp", "python"], required=True)

    return parser

def main():
    parser = init_argparse()
    args = vars(parser.parse_args())
    
    base_path = os.path.abspath(os.path.dirname(__file__))
    file = os.path.join(base_path, "templates", args["language"] + ".txt")
    destination = os.path.join(os.getcwd(), ".gitignore")

    shutil.copy(file, destination)

if __name__ == "__main__":
    main()
