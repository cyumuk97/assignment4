#!/usr/bin/env python3
# intersection.py

"""
Finds all gene symbols in both chr21_genes.txt and HUGO_genes.txt
"""
import os
import argparse
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
    I2 = "HUGO_genes.txt"

    # Output file
    outfile = "intersection_output.txt"

    # Get file objects
    fh_in1 = my_io.get_fh(I1, "r")
    fh_in2 = my_io.get_fh(I2, "r")

    # Get sets
    U21, UH, C = get_sets(fh_in1, fh_in2)

    # Prepare output variables
    unique_21 = "Number of unique gene names in chr21_genes.txt: " + str(len(U21))
    unique_hugo = "Number of unique gene names in HUGO_genes.txt: " + str(len(UH))
    common = "Number of common gene symbols found: " + str(len(C))
    end_line = "Output stored in OUTPUT/intersection_output.txt"

    final = unique_21 + "\n" + unique_hugo + "\n" + common + "\n" + end_line

    # Path to output directory
    
    # Save path
    SP = '/OUTPUT'

    # Out path
    OP = os.path.join(SP, outfile)
                    
    # Store set elements
    store = ""
    for elem in C:
        store += str(elem) + "\n"
                                                
    # Write to file
    fh_out = my_io.get_fh(outfile, "w")
    fh_out.write(store)
    fh_out.close()

def get_sets(file21, hugo):

    """
    Returns sets containing common and unique gene names
    """

    # Initiate lists for chr_21 and HUGO
    C21 = []
    H = []

    # Store the lines of text files in appropriate lists
    for line in file21:
        C21.append(line.split("\t"))

    for line in hugo:
        H.append(line.split("\t"))

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

    return U21, UH, C

def get_cli_args():

    """
    Gets command line options using argparse
    """
    parser = argparse.ArgumentParser(
            description='Provide two gene list (ignore header line), find intersection')

    parser.add_argument('-i1', '--infile1',
            dest='INFILE1',
            type=str,
            help='Gene list 1 to open',
            required=True)

    parser.add_argument('-i2', '--infile2',
            dest='INFILE2',
            type=str,
            help='Gene list 2 to open',
            required=True)

    return parser.parse_args()

if __name__ == '__main__':
    main()
