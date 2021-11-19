from Sample import Sample
from Dataset import Dataset

def loadCSV(path):
    file = open(path,'r')
    
    header = file.readline()
    header = header.replace("\n","")
    dataset = Dataset(header.split(","))
    
    for line in file:
        line = line.replace("\n","")
        sample = Sample(dataset.getAttributes(),line.split(","))
        dataset.addSample(sample)
    
    file.close()
    return dataset