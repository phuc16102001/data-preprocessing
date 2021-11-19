import argparse
import os
import sys
from FileHandler import *
from Dataset import *

parser = argparse.ArgumentParser(description="Impute the missing data")

parser.add_argument("path",
                    action='store',
                    type=str,
                    help='the path to csv file')

parser.add_argument("--mode",
                    action='store',
                    choices=['mode','mean','median'],
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
mode = args['mode']
columns = args['columns']

try:
    df = loadCSV(inputPath)
    for column in columns:
        df.fillMissingAttribute(column,mode)
    exportCSV(outputPath,df)
except ValueError as e:
    print(e)