from FileHandler import *

dataset = loadCSV("data/mydat.csv")
print("Number of samples:",dataset.count())
print("Missing class\n",dataset.missingAttribute())
print("Number of missing samples:",dataset.countMissingSample())

dataset.removeDuplicated()
exportCSV("output/output.csv", dataset)