import argparse
import os
import sys
from FileHandler import *
from Dataset import *

parser = argparse.ArgumentParser(description="List the missing data")

parser.add_argument("path",
                    action='store',
                    type=str,
                    help='the path to csv file')

args = vars(parser.parse_args())

inputPath = args['path']

df = loadCSV(inputPath)
print("Number of samples:",df.count())
print("Number of missing samples:",df.countMissingSample())

missingAttribute = df.missingAttribute()
print("The missing attribute:")
for attribute in missingAttribute.keys():
    print("\t%s: %d"%(attribute,missingAttribute[attribute]))