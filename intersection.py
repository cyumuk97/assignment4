#!/usr/bin/env python3
# intersection.py

"""
Finds all gene symbols in both chr21_genes.txt and HUGO_genes.txt
"""
import os
import argparse
from assignment4 import my_io

# Initiate lists for chr_21 and HUGO
C21 = []
H = []

# Store the lines of text files in appropriate lists

