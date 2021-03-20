#!/usr/bin/env python3
# categories.py

"""
Counts how many genes are in each category in chr21_genes.txt
"""

import argparse
import os
from assignment4 import my_io

# Initiate a list to store data from file
GL = []

# Initiate a list to store gene categories
GC = []

# Initiate a dictionary
GD = {}

# Open file and store data in gene list
I = my_io.get_fh("chr21_genes.txt", "r")

for line in I:
    GL.append(line.split("\t"))

I.close()

# Store gene categories
for i in range(1, len(GL)):
    GC.append(GL[i][2].replace('\n', ''))

# Sort gene categories
GC.sort()

# Initiate a list to store singular categories
SC = []

# Loop through gene categories
for i in range(1, len(GC)):
    if GC[i] not in SC:
        SC.append(GC[i])

# Initiate a dictionary for category meanings
GM = dict.fromkeys(SC)

# Gene meanings
M11 = "Genes with 100% identity over a complete cDNA with defined functional\
        association (for example, transcription factor, kinase)."

M12 = "Genes with 100% identity over a complete cDNA corresponding to a gene\
        of unknown function (for example, some of the KIAA series of large cDNAs)."

M21 = "Genes showing similarity or homology to a characterized cDNA from any\
        organism (25–100% amino-acid identity)."

M22 = "Genes with similarity to a putative ORF predicted in silico from the\
        genomic sequence of any organism but which currently lacks\
        experimental verification."

M31 = "Genes with amino-acid similarity confined to a protein region specifying\
        a functional domain (for example, zinc fingers, immunoglobulin domains)."

M32 = "Genes with amino-acid similarity confined to regions of a known protein\
        without known functional association."

M41 = "Predicted genes composed of a pattern of two or more consistent exons\
        (located within <20 kb) and supported by spliced EST match(es)."

M42 = "Predicted genes corresponding to spliced EST(s) but which failed to\
        be recognized by exon prediction programs."

M43 = "Predicted genes composed only of a pattern of consistent exons\
        without any matches to ETS(s) or cDNA."

M5 = "Pseudogenes may be regarded as gene-derived DNA sequences that\
        are no longer capable of being expressed as protein products."

# List of gene meanings
S = [M11, M12, M21, M22, M31, M32, M41, M42, M43, M5]

# Store meanings in gene meanings dictionary
for i in range(len(GM)):
    GM[SC[i]] = S[i]

# Store categories in category dictionary
for category in GC[1:]:
    GD[category] = GD.get(category,0) + 1

# Prepare output variables
header = "Category\tOccurrence\tDescription"
info = ""

# Add to info
for (k, v) in GD.items():
    info += str(k) + "\t" + str(v) + "\t" + str(GM[k]) + "\n"

# Create final output
final = header + "\n" + info

# Prepare output file
O = my_io.get_fh("categories.txt", "w")

# Path to output directory

# Save path
SP = 'assignment4/OUTPUT'

# Out path
OP = os.path.join(SP,O)

# Write final output to file

