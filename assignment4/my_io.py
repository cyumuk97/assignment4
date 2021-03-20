#!/usr/bin/env python3
# my_io.py

"""
Opens files with get_fh function
"""


def get_fh(filename, openfile):
    """
    Opens an input file and passes back a file object
    """
    try:
        newfile = open(filename, openfile)
        return newfile
    except IOError:
        raise IOError(f"Cannot open the file {filename} for type '{openfile}'")
    except ValueError:
        raise ValueError(f"Cannot open the file {filename} for type '{openfile}'")
