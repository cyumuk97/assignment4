#!/usr/bin/env python3
# chr21-gene_names.py

"""
Asks user to enter a gene symbol and prints its description
"""
import argparse
from assignment4 import my_io

def main():
    """
    Main function
    """
    args = get_cli_args()
    infile = args.infile

# Initiate a list to store data from file
GL = []

# Initiate a list to store gene symbols
GS = []

# Initiate a list to store gene descriptions
GD = []

# Open the file and store the information in gene_list
I = my_io.get_fh("chr21_genes.txt", "r")

for line in I:
    GL.append(line.split("\t"))

I.close()

# Store gene symbols in gene_symbol
for i in range(1, len(GL)):
    GS.append(GL[i][0])

# Store gene descriptions in gene_description
for j in range(1, len(GL)):
    GD.append(GL[j][1])

# Initiate a dictionary
D = dict.fromkeys(GS)

# Enter values to dictionary
for i in range(len(D)):
    D[GS[i]] = GD[i]

# Initiate a loop for inputs
while True:
    GI = input("Enter gene name of interest. Type quit to exit: ")

    if GI.lower() == "quit":
        print("Thanks for querying the data.")
        break

    if GI in D:
        print(GI + " " + "found! Here is the description:")
        print(D[GI])

    else:
        print("Not a valid gene name")

def get_cli_args():
    """
    Gets command line options using argparse
    Returns instances of argparse arguments
    """
    parser = argparse.ArgumentParser(
        description='Open chr21_genes.txt, and ask user for a gene name')

    parser.add_argument('-i', '--infile',
                        dest='INFILE',
                        type=str,
                        help='Path to the file to open',
                        required=True)

    return parser.parse.args()
