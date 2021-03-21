#!/usr/bin/env python3
# test_my_io.py

"""
Tests the programs
"""
import os
import pytest
from assignment4 import (chr21_gene_names, categories, intersection)

test = "test_21.txt"

def test_chr21_gene_names():
    """
    Tests chr21_gene_name.py
    """
    infile = _create_test_file("chr21_genes.txt", test)



    # Test
    test_chr21 = chr21_gene_names(

def _create_test_file(filename, test):
    """
    Helper function to create file for testing
    """
    fh_in = open(filename, "r")
    fh_out = open(test, "w")
