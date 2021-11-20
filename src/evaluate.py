import argparse
import os
import sys
from FileHandler import *
from Dataset import *

parser = argparse.ArgumentParser(description="Evaluate a new attribute")

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

args = vars(parser.parse_args())

inputPath = args['path']
expression = args['expression']
outPath = args['out']

dataset = loadCSV(inputPath)
dataset.addAttributeExpression(expression)
exportCSV(outPath, dataset)