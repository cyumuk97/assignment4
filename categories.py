#!/usr/bin/env python3
# categories.py

"""
Counts how many genes are in each category in chr21_genes.txt
"""

import argparse
import os
from assignment4 import my_io

def main():
    """
    Main function
    """
    args = get_cli_args()
    I1 = args.INFILE1
    I2 = args.INFILE2

    # Input files
    I1 = "chr21_genes.txt"
    I2 = "chr21_genes_categories.txt"

    # Output file
    outfile = "categories.txt"

    # Get file objects with get_fh
    fh_in1 = my_io.get_fh(I1, "r")
    fh_in2 = my_io.get_fh(I2, "r")

    # Initiate a list to store data from file
    GL = []

    # Initiate a list to store gene categories
    GC = []

    # Initiate a dictionary
    GD = {}

    # Store lines in list
    for line in fh_in1:
        GL.append(line.split("\t"))

    fh_in1.close()

    # Store gene categories
    for i in range(1, len(GL)):
        GC.append(GL[i][2].replace('\n', ''))

    # Sort gene categories
    GC.sort()

    # Store categories in category dictionary
    for category in GC[1:]:
        GD[category] = GD.get(category,0) + 1

    # Create a list for the file of gene meanings
    GM = []

    # Store lines in gene meaning list
    for line in fh_in2:
        GM.append(line.split("\t"))

    fh_in2.close()

    # Turn gene meanings list into a dictionary
    DM = dict(GM)

    # Prepare output variables
    header = "Category\tOccurrence\tDescription"
    info = ""

    # Add to info
    for (k, v) in GD.items():
        info += str(k) + "\t" + str(v) + "\t" + str(DM[k]) + "\n"

    # Create final output
    final = header + "\n" + info

    # Path to output directory

    # Save path
    SP = '/OUTPUT'

    # Out path
    OP = os.path.join(SP, outfile)
    print(OP)

    # Write to file
    with open(OP, "w") as out:
        out.write(final)
    out.close()

def get_cli_args():
    """
    Gets command line options using argparse
    """
    parser = argparse.ArgumentParser(
            description='Combine on gene name and count the category occurrence')

    parser.add_argument('-i1', '--infile1',
                        dest='INFILE1',
                        type=str,
                        help='Path to the gene description file to open',
                        required=True)

    parser.add_argument('-i2', '--infile2',
                        dest='INFILE2',
                        type=str,
                        help='Path to the gene category to open',
                        required=True)

    return parser.parse_args()

if __name__ == '__main__':
    main()
