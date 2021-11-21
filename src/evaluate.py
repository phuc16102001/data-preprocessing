import argparse
import os
import sys
from FileHandler import *
from Dataset import *

# Create parser
parser = argparse.ArgumentParser(description="Evaluate a new attribute")

# Add arguments
parser.add_argument("path",
                    action='store',
                    type=str,
                    help='the path to csv file')
parser.add_argument("--expression",
                    action='store',
                    required=True,
                    type=str)
parser.add_argument("--out",
                    action='store',
                    type=str,
                    required=True)

# Extract arguments
args = vars(parser.parse_args())
inputPath = args['path']
expression = args['expression']
outPath = args['out']

# Main process
try:
    dataset = loadCSV(inputPath)
    dataset.addAttributeExpression(expression)
    exportCSV(outPath, dataset)
except (FileNotFoundError) as e:
    print(e)