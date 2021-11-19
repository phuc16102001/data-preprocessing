import argparse
import os
import sys
from FileHandler import *
from Dataset import *

parser = argparse.ArgumentParser(description="Remove duplicated samples")

parser.add_argument("path",
                    action='store',
                    type=str,
                    help='the path to csv file')

parser.add_argument("--out",
                    action='store',
                    type=str,
                    required=True)

args = vars(parser.parse_args())

inputPath = args['path']
outputPath = args['out']

try:
    df = loadCSV(inputPath)
    df.removeDuplicated()
    exportCSV(outputPath,df)
except ValueError as e:
    print(e)