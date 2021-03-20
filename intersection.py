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
F21 = my_io.get_fh("chr21_genes.txt", "r")
HUGO = my_io.get_fh("HUGO_genes.txt", "r")

for line in F21:
    C21.append(line.split("\t"))

F21.close()

for line in HUGO:
    H.append(line.split("\t"))

HUGO.close()

# Initiate sets
S21 = set()
SH = set()

# Store data in sets
for i in range(1,len(C21)):
    S21.add(C21[i][0])

for i in range(1,len(H)):
    SH.add(H[i][0])

# Symbols unique to chr21_genes.txt
U21 = S21 - SH

# Symbols unique to HUGO_genes.txt
UH = SH - S21

# Common symbols
C = S21 & SH
