import argparse
import os
import sys
from FileHandler import *
from Dataset import *

def normalizeRestrict(value):
    try:
        value = float(value)
    except:
        raise argparse.ArgumentTypeError("%r not a floating-point number"%(value,))
    if (value<0.0 or value>1.0):
        raise argparse.ArgumentTypeError("%r not not in range [0,1]"%(value,))
    return value

parser = argparse.ArgumentParser(description="Remove using threshold")

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

args = vars(parser.parse_args())

inputPath = args['path']
outputPath = args['out']
axis = args['axis']
threshold = args['threshold']

df = loadCSV(inputPath)
if (axis=='sample'):
    df.removeSamples(threshold)
elif (axis=='attribute'):
    df.removeAttributes(threshold)
exportCSV(outputPath,df)