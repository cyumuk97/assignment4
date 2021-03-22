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
    in_1 = args.INFILE1
    in_2 = args.INFILE2

    # Input files
    in_1 = "chr21_genes.txt"
    in_2 = "HUGO_genes.txt"

    # Output file
    outfile = "intersection_output.txt"

    # Get file objects
    fh_in1 = my_io.get_fh(in_1, "r")
    fh_in2 = my_io.get_fh(in_2, "r")

    # Get sets
    chromosome, hugo, common = get_sets(fh_in1, fh_in2)

    # Output
    string = "Number of unique gene names in chr21_genes.txt: "
    print(string + str(len(chromosome)))
    print("Number of unique gene names in HUGO_genes.txt: " + str(len(hugo)))
    print("Number of common gene symbols found: " + str(len(common)))
    print("Output stored in OUTPUT/intersection_output.txt")

    # Path to output directory
    # Save path
    save = '/OUTPUT'

    # Out path
    out = os.path.join(save, outfile)

    # Store set elements
    store = ""
    for elem in common:
        store += str(elem) + "\n"

    # Write to file
    fh_out = my_io.get_fh(out, "w")
    fh_out.write(store)
    fh_out.close()


def get_sets(file21, hugo):

    """
    Returns sets containing common and unique gene names
    """

    # Initiate lists for chr_21 and HUGO
    list_chromosome = []
    list_hugo = []

    # Store the lines of text files in appropriate lists
    for line in file21:
        list_chromosome.append(line.split("\t"))

    for line in hugo:
        list_hugo.append(line.split("\t"))

    # Initiate sets
    set_chromosome = set()
    set_hugo = set()

    # Store data in sets
    for i in range(1, len(list_chromosome)):
        set_chromosome.add(list_chromosome[i][0])

    for i in range(1, len(list_hugo)):
        set_hugo.add(list_hugo[i][0])

    # Symbols unique to chr21_genes.txt
    unique_chromosome = set_chromosome - set_hugo

    # Symbols unique to HUGO_genes.txt
    unique_hugo = set_hugo - set_chromosome

    # Common symbols
    common = set_chromosome & set_hugo

    return unique_chromosome, unique_hugo, common


def get_cli_args():

    """
    Gets command line options using argparse
    """
    parser = argparse.ArgumentParser(
        description='Provide two gene lists, find intersection')

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
