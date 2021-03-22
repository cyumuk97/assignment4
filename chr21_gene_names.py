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
    infile = args.INFILE

    # Output files
    infile = "chr21_genes.txt"

    # Get file object with get_fh
    fh_in = my_io.get_fh(infile, "r")

    # Get Dictionary
    dictionary = get_gene_names(fh_in)

    # Initiate a loop for inputs
    while True:
        gene = input("Enter gene name of interest. Type quit to exit: ")

        if gene.lower() == "quit":
            print("Thanks for querying the data.")
            break

        if gene in dictionary:
            print(gene + " " + "found! Here is the description:")
            print(dictionary[gene])

        else:
            print("Not a valid gene name")


def get_gene_names(filename):

    """
    Returns a dictionary that stores gene names
    """
    # Initiate a list to store data from file
    data = []

    # Initiate a list to store gene symbols
    symbol = []

    # Initiate a list to store gene descriptions
    description = []

    # Open the file and store the information in gene_list
    for line in filename:
        data.append(line.split("\t"))

    # Store gene symbols in gene_symbol
    for i in range(1, len(data)):
        symbol.append(data[i][0])

    # Store gene descriptions in gene_description
    for j in range(1, len(data)):
        description.append(data[j][1])

    # Initiate a dictionary
    dictionary = dict.fromkeys(symbol)

    # Enter values to dictionary
    for i in range(len(dictionary)):
        dictionary[symbol[i]] = description[i]

    return dictionary


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

    return parser.parse_args()


if __name__ == '__main__':
    main()
