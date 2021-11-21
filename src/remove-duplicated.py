import argparse
import os
import sys
from FileHandler import *
from Dataset import *

# Create parser
parser = argparse.ArgumentParser(description="Remove duplicated samples")

# Add arguments
parser.add_argument("path",
                    action='store',
                    type=str,
                    help='the path to csv file')
parser.add_argument("--out",
                    action='store',
                    type=str,
                    required=True)

# Extract arguments
args = vars(parser.parse_args())
inputPath = args['path']
outputPath = args['out']

# Main process
try:
    df = loadCSV(inputPath)
    df.removeDuplicated()
    exportCSV(outputPath,df)
except (FileNotFoundError,ValueError) as e:
    print(e)