#!/usr/bin/env python3
# categories.py

"""
Counts how many genes are in each category in chr21_genes.txt
"""

import argparse
import os.path
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
    in_2 = "chr21_genes_categories.txt"

    # Output file
    outfile = "categories.txt"

    # Get file objects with get_fh
    fh_in1 = my_io.get_fh(in_1, "r")
    fh_in2 = my_io.get_fh(in_2, "r")

    # Get dictionaries
    gene, meaning = gene_count(fh_in1, fh_in2)
    print(len(gene))
    print(len(meaning))

    # Prepare output variables
    header = "Category\tOccurrence\tDescription"
    info = ""

    # Add to info
    for (key, value) in gene.items():
        info += str(key) + "\t" + str(value) + "\t" + str(meaning[key]) + "\n"

    # Path to output directory
    # Save path
    save = 'OUTPUT/'

    # Out path
    out = os.path.join(save, outfile)

    # Write to file
    fh_out = my_io.get_fh(out, "w")
    fh_out.write(header + "\n" + info)
    fh_out.close()


def gene_count(cat, meaning):
    """
    Returns two dictionaries with gene meanings and gene categories
    """

    # Initiate a list to store data from file
    lines = []

    # Initiate a list to store gene categories
    category = []

    # Initiate a dictionary
    dictionary = {}

    # Store lines in list
    for line in cat:
        lines.append(line.split("\t"))

    # Store gene categories
    for i in range(1, len(lines)):
        category.append(lines[i][2].replace('\n', ''))

    # Sort gene categories
    category.sort()

    # Store categories in category dictionary
    for categories in category[1:]:
        dictionary[categories] = dictionary.get(categories, 0) + 1

    # Create a list for the file of gene meanings
    meanings = []

    # Store lines in gene meaning list
    for line in meaning:
        meanings.append(line.split("\t"))

    # Turn gene meanings list into a dictionary
    mean = dict(meanings)

    return dictionary, mean


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
