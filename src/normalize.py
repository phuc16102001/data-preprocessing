import argparse
import os
import sys
from FileHandler import *
from Dataset import *

# Create parser
parser = argparse.ArgumentParser(description="Normalize the value")

# Add arguments
parser.add_argument("path",
                    action='store',
                    type=str,
                    help='the path to csv file')
parser.add_argument("--method",
                    action='store',
                    choices=['min-max','z-score'],
                    required=True,
                    type=str)
parser.add_argument("--columns",
                    action='store',
                    required=True,
                    nargs='*',
                    type=str,
                    default=[])
parser.add_argument("--out",
                    action='store',
                    type=str,
                    required=True)

# Extract arguments
args = vars(parser.parse_args())
inputPath = args['path']
outputPath = args['out']
method = args['method']
columns = args['columns']

# Main process
try:
    df = loadCSV(inputPath)
    for column in columns:
        df.normalizeAttribute(column, method)
    exportCSV(outputPath,df)
except (FileNotFoundError,ValueError) as e:
    print(e)