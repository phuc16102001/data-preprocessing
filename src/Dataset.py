from Sample import Sample
import math

class Dataset:
    lsAttribute = []
    data = []
    
    """
    Initialize the dataset with a list of attributes
    
    Args:
        attributes: a list of string, list of attributes for dataset
    """
    def __init__(self, attributes):
        self.data = []
        self.lsAttribute = attributes.copy()
    
    """
    Getter for attribute list
    
    Returns:
        list: a list of String, the attribute list
    """
    def getAttributes(self):
        return self.lsAttribute.copy()
    
    """
    Add a new sample to dataset
    
    Args:
        sample: a Sample object, the adding sample
    """
    def addSample(self, sample):
        self.data.append(sample)
        
    """
    Count the number of sample
    
    Returns:
        count: an integer number, the number of samples
    """
    def count(self):
        return len(self.data)
    
    """
    Get the sample of a specified index
    
    Args:
        index: the index of sample
    Returns:
        sample: a Sample object, the requesting sample
    """
    def getSample(self,index):
        return self.data[index]

    """
    Add a new attribute with the value of samples for that attribute
    
    Args:
        attributeName: a string, name of the adding attribute
        sampleValues: a list of string, the value of adding attribute for each sample 
    """
    def addAttribute(self, attributeName, sampleValues):
        self.lsAttribute.append(attributeName)
        for i in range(len(data)):
            try:
                self.data[i][attributeName] = float(sampleValues[i])
            except:
                self.data[i][attributeName] = sampleValues[i]
        
    """ 
    Finding missing attributes and count number of missing sample for each
    
    Args:
        nothing
    Returns:
        dict: A dictionary structure contains missing attributes as key, 
        and number of missing sample as value
    """
    def missingAttribute(self):                           
        result = dict()
        for attribute in self.lsAttribute:
            for sample in self.data:
                value = sample.getValue(attribute)
                if (value==""):
                    if (attribute in result):
                        result[attribute] += 1
                    else:
                        result[attribute] = 1
        return result

    """
    Count the number of missing sample (sample that has one or more missing value)
    
    Args:
        nothing
    Returns:
        count: A integer number, the number of missing sample
    """
    def countMissingSample(self):                           
        count = 0
        for sample in self.data:
            if (sample.isMissing()):
                count += 1
        return count

    """
    Fill the missing value of an attribute with methods
    
    Args:
        attributeName: the name of attribute need to fill
        method: the method name (Median, Mode, Mean)
    Returns:
        nothing
    """
    def fillMissingAttribute(self, attributeName, method = "Median"):  #3
        listValueAttribute = []
        fillValue = None

        for sample in self.data:
            temp = sample.getValue(attributeName)
            if temp != "":
                listValueAttribute.append(temp)

                if type(temp) == str:
                    method = "Mode"

        if method == "Mode":
            listAttributeFre = {}
            for value in listValueAttribute:
                listAttributeFre[value] += 1
            fillValue = max(listAttributeFre, key=listAttributeFre.get)
        elif method == "Median":
            sorted(listValueAttribute)
            if len(listValueAttribute) % 2 == 1:
                mid = len(listValueAttribute)//2 + 1
                fillValue = listValueAttribute[mid]
            else:
                mid = len(listValueAttribute) // 2
                fillValue = (listValueAttribute[mid] + listValueAttribute[mid+1])/2
        elif method == "Mean":
            sum = 0
            for value in listValueAttribute:
                sum += value
            fillValue = sum / len(listValueAttribute)

        for sample in self.data:
            temp = sample.getValue(attributeName)
            if temp == "":
                sample.setValue(attributeName, fillValue)

    """
    Normalize the attributes with different methods
    
    Args:
    Returns:
    """
    def normalizeAttribute(self, attributeName, method = "min-max"):
        listValueAttribute = []

        for sample in self.data:
            temp = sample.getValue(attributeName)
            if temp != "":
                listValueAttribute.append(temp)

                if type(temp) == str:
                    print("ahihihi") #cái này cần m tự bắt =))

        if method == "min-max":
            minValue = min(listValueAttribute)
            maxValue = max(listValueAttribute)
            for sample in self.data:
                value = sample.getValue(attributeName)
                if value != "":
                    normalizeValue = (value - minValue) / (maxValue - minValue)
                    sample.setValue(attributeName, normalizeValue)
        elif method == "z-score":
            mean = sum(listValueAttribute) / len(listValueAttribute)
            std = 0
            for value in listValueAttribute:
                std += (value - mean)**2
            std = math.sqrt(std / len(listValueAttribute))

            for sample in self.data:
                value = sample.getValue(attributeName)
                if value != "":
                    normalizeValue = (value - mean) / std
                    sample.setValue(attributeName, normalizeValue)
