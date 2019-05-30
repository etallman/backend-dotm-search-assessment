#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import zipfile
import argparse

# iterate through dotm files/managing files
def manage_file(filename, search_term):
    """Function conducts an outer and inner zip to search the folder for .dotm files and then searches the text for matches."""
    # Outer Zip
    if not zipfile.is_zipfile(filename):
        print("Error: not a zipfile.")
        return 0
    with zipfile.ZipFile(filename) as zip:
        print(zip.namelist())
    #Inner Zip#
        with zip.open('word/document.xml') as doc:
            # print("Searching directory " + namespace.folder)
            for line in doc:
                index = str(line).find(search_term)
                if index >= 0:
                    print("Match found in file {}".format(filename))
                    print(" ..." + line[index-40:index+40] + "...")
                    return True
            return False


# Inspection function
def file_parser():
    """Function parses the folders and files."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder", help="Dotm folder to search.")
    parser.add_argument("text", help="Text to search.")
    return parser


#  """Function prints test results to output file."""
__author__ = "Eileen with help from instructor"


def main():
    files_searched = 0
    matches = 0
    parser = file_parser()
    namespace = parser.parse_args()
    for f in os.listdir(namespace.folder):
        if not f.endswith(".dotm"):
            print("Not a .dotm -- skipping file {}".format(f))
            continue
        files_searched +=1
        full_path = os.path.join(namespace.folder, f)
        if manage_file(full_path, namespace.text):
            matches +=1
    print("Total files searched: {}".format(files_searched))
    print("Total matches found: {}".format(matches))

if __name__ == '__main__':
    main()