from Utils import *

dataset = loadCSV("data/house-prices.csv")
print(dataset.count())
print(dataset.missingAttribute())
print(dataset.getSample(0))