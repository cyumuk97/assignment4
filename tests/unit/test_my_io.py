#!/usr/bin/env python3
# test_my_io.py

"""
Tests the programs
"""
import os
import pytest
from assignment4 import (chr21_gene_names, categories, intersection)

test = "test.txt"

def test_chr21_gene_naes():
    """
    Tests chr21_gene_name.py
    """
    _create_test_file(

def _create_test_file(filename):
    """
    Helper function to create file for testing
    """
    open(filename, "w").close()
