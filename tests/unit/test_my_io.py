#!/usr/bin/env python3
# test_my_io.py

"""
Tests the programs
"""
import os
import pytest
from assignment4 import my_io
from chr21_gene_names import get_gene_names
from categories import gene_count
from intersection import get_sets

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
    dictionary = get_gene_names(chromosome)
    with pytest.raises(SystemExit):
        assert len(dictionary) == 285


def test_gene_count():
    """
    Tests gene_count function
    """
    # Create test file
    _create_test_file(test2)

    # Test the function
    dictionary, meaning = gene_count(chromosome, chromosome_categories)
    assert len(dictionary) == len(meaning)


def test_get_sets():
    """
    Tests get_sets function
    """
    # Create test file
    _create_test_file(test3)

    # Test the function
    unique_chromosome, unique_hugo, common = get_sets(chromosome, hugo)
    assert len(unique_chromosome) == 81
    assert len(unique_hugo) == 11611
    assert len(common) == 204


def _create_test_file(filename):
    """
    Helper function to create file for testing
    """
    open(filename, "w").close()
