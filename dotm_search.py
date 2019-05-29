#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a directory path, search all files in the path for a given text string
within the 'word/document.xml' section of a MSWord .dotm file.

Write a python program named `dotm_search.py`.  
Your program should accept two cmdline arguments: First argument is the text to search for. 
The second argument is an OPTIONAL directory of .dotm files to scan.  If this argument is omitted,
the default path to search is the current directory.  NOTE that the optional directory `--dir [dotm-path]` actually includes two arguments (the option flag, and its value) but we are counting them as one combined argument key-value pair.
```
python dotm_search.py --dir ./dotm_files "$" 
python dotm_search.py "other text"
```

- Your program should print the full path name of each file that was found to contain the search text.  If the file contains multiple matches, just count it as a single match.
- For context, print a partial line of the dotm text that was found to contain the search text.  Limit the printed line to +/- 40 characters on each side of the matched text.  Example: `"...alculated on a per article basis (up to $500 each), the total false marking penal..."`
- Count the total number of file matches as well as total number of files searched, and display the results before exiting.
"""
import my_module as mm
import sys

# courses = ['History', 'Math', 'Physics', 'CompSci']
# pricing_info = mm.find_pricing(courses, 'Math')
# print(pricing_info)

print(sys.path)
# import zip 
# get documentation
# extract xml
#  """Function prints test results to output file."""

#     with open('input.txt', "r+") as rf:
#         with open('output.txt', 'w') as wf:    
#             for line in rf:
#                 wf.write(nested_brackets(line)+'\n')

__author__ = "etallman"


def main():
    # raise NotImplementedError("Your awesome code begins here!")
    print('dotm_search')
    
if __name__ == '__main__':
    main()