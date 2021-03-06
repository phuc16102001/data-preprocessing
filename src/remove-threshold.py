import argparse
import os
import sys
from FileHandler import *
from Dataset import *

"""
Function to check normalize arguments
Args:
    value: the value we need to check
Returns:
    value: return the input value if valid
Exceptions:
    ArgumentTypeError: if not numeric or not in range [0,1]
"""
def normalizeRestrict(value):
    try:
        value = float(value)
    except:
        raise argparse.ArgumentTypeError("%r not a floating-point number"%(value,))
    if (value<0.0 or value>1.0):
        raise argparse.ArgumentTypeError("%r not not in range [0,1]"%(value,))
    return value

# Create parser
parser = argparse.ArgumentParser(description="Remove using threshold")

# Add arguments
parser.add_argument("path",
                    action='store',
                    type=str,
                    help='the path to csv file')
parser.add_argument("--axis",
                    action='store',
                    choices=['sample','attribute'],
                    required=True,
                    type=str)
parser.add_argument("--threshold",
                    action='store',
                    required=True,
                    type=normalizeRestrict)
parser.add_argument("--out",
                    action='store',
                    type=str,
                    required=True)

# Extract arguments
args = vars(parser.parse_args())
inputPath = args['path']
outputPath = args['out']
axis = args['axis']
threshold = args['threshold']

try:
    df = loadCSV(inputPath)
    if (axis=='sample'):
        df.removeSamples(threshold)
    elif (axis=='attribute'):
        df.removeAttributes(threshold)
    exportCSV(outputPath,df)
except (FileNotFoundError) as e:
    print(e)