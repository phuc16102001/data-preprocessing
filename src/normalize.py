import argparse
import os
import sys
from FileHandler import *
from Dataset import *

parser = argparse.ArgumentParser(description="Normalize the value")

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

args = vars(parser.parse_args())

inputPath = args['path']
outputPath = args['out']
method = args['method']
columns = args['columns']

try:
    df = loadCSV(inputPath)
    for column in columns:
        df.normalizeAttribute(column, method)
    exportCSV(outputPath,df)
except ValueError as e:
    print(e)