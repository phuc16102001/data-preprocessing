from FileHandler import *

dataset = loadCSV("data/mydat.csv")
print("Number of samples:",dataset.count())
print("Missing class\n",dataset.missingAttribute())
print("Number of missing samples:",dataset.countMissingSample())

dataset.normalizeAttribute('Score', method='z-score')
exportCSV("output/output.csv", dataset)