#!/usr/bin/env python3
# test_my_io.py

"""
Tests the programs
"""
import os
import pytest
#from /home/yumuk.c/programming6200/assignment4 import my_io
from chr21_gene_names import get_gene_names
from categories import gene_count
from intersection import get_sets

# Directory
basepath = '/home/yumuk.c/programming6200/assignment4/'
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name)
# Files to test
chromosome = "../chr21_genes.txt"
chromosome_categories = "../chr21_genes_categories.txt"
hugo = "../HUGO_genes.txt"

test1 = "test_21.txt"
test2 = "test_categories.txt"
test3 = "test_intersection.txt"

def test_get_gene_names():
    """
    Tests get_gene_names
    """
    # Create test file
    _create_test_file(test1)

    # Test the function
    test = my_io.get_fh(test1, "r")
    D = get_gene_names(chromosome)
    assert len(D) == 285

def test_gene_count():
    """
    Tests gene_count function
    """
    # Create test file
    _create_test_file(test2)

    # Test the function


def _create_test_file(filename):
    """
    Helper function to create file for testing
    """
    open(filename, "w").close()
