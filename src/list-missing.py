import argparse
import os
import sys
from FileHandler import *
from Dataset import *

# Create parser
parser = argparse.ArgumentParser(description="List the missing data")

# Add arguments
parser.add_argument("path",
                    action='store',
                    type=str,
                    help='the path to csv file')

# Extract arguments
args = vars(parser.parse_args())
inputPath = args['path']

# Main process
try:    
    df = loadCSV(inputPath)
    print("Number of samples:",df.count())
    print("Number of missing samples:",df.countMissingSample())

    missingAttribute = df.missingAttribute()
    print("The missing attribute:")
    for attribute in missingAttribute.keys():
        print("\t%s: %d"%(attribute,missingAttribute[attribute]))
except (FileNotFoundError) as e:
    print(e)