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
    
    base_path = os.path(__file__)
    file = os.path.join(base_path, "templates", args["l"])
    destination = os.path.join(os.curdir(), ".gitignore")

    shutil.copy(file, destination)
