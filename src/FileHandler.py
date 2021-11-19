from Dataset import Dataset
from Sample import Sample

"""
Load a dataframe from the CSV files

Args:
    path: the absolute or relative path direct to the CSV file
Returns:
    dataset: the Dataset object loaded from CSV file
"""
def loadCSV(path):
    file = open(path,'r')
    
    # Read header and create dataset
    header = file.readline()
    header = header.replace("\n","")
    dataset = Dataset(header.split(","))
    
    # Read samples
    for line in file:
        line = line.replace("\n","")
        sample = Sample(dataset.getAttributes(),line.split(","))
        dataset.addSample(sample)
    
    file.close()
    return dataset

"""
Export a dataframe to CSV file

Args:
    path: the absolute or relative path direct to the file we want to export
    dataset: the Dataset object which we want to export
"""
def exportCSV(path, dataset):
    file = open(path,'w')
    
    # Export header
    attributes = dataset.getAttributes()
    line = ""
    for attribute in attributes:
        line += str(attribute)+","
    file.write(line[:-1]+"\n")
    
    # Export samples
    for i in range(dataset.count()):
        sample = dataset.getSample(i)
        line = ""
        for attribute in attributes:
            line += str(sample.getValue(attribute))+","
        file.write(line[:-1]+"\n")
    
    file.close()