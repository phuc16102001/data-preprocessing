from Sample import Sample
from Utils import *
import math

class Dataset:
    """
    Attribute:
        lsAttribute: the list of attribute header
        data: samples of data frame, each sample is a Sample object
    """
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
    
    Returns:
        dict: A dictionary structure contains missing attributes as key, and number of missing sample as value
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
        method: the method name (Median, Mode, Mean), the argument is not case-sensitive
    """
    def fillMissingAttribute(self, attributeName, method):
        method = method.upper()
        
        lsValue = []
        for sample in self.data:
            value = sample.getValue(attributeName)
            if value == "":
                continue
            if (type(value) == str) and (method!="MODE"):
                raise ValueError("Method for nomial attribute must be method=\"MODE\"")
            lsValue.append(value)
        
        fillValue = None
        if method == "MODE":
            fillValue = findMode(lsValue)
        elif method == "MEDIAN":
            fillValue = findMedian(lsValue)
        elif method == "MEAN":
            fillValue = findMean(lsValue)

        for sample in self.data:
            value = sample.getValue(attributeName)
            if value == "":
                sample.setValue(attributeName, fillValue)

    """
    Normalize the attributes with different methods
    
    Args:
        attributeName: the name of attribute need to normalize
        method: the method name (Min-max, Z-score), the argument is not case-sensitive
    """
    def normalizeAttribute(self, attributeName, method):
        method = method.upper()
        
        lsValue = []
        for sample in self.data:
            value = sample.getValue(attributeName)
            if (value == ""):
                continue
            if (type(value) == str):
                raise ValueError("You can only normalize for numeric attribute")
            lsValue.append(value)

        minValue = min(lsValue)
        maxValue = max(lsValue)
        mean = findMean(lsValue)
        std = findStd(lsValue)

        for sample in self.data:
            value = sample.getValue(attributeName)
            if (value==""):
                continue
            if (method=="MIN-MAX"):
                normalizeValue = normalizeMinMax(minValue, maxValue, value)
            elif (method=="Z-SCORE"):
                normalizeValue = normalizeZScore(mean,std,value)
            sample.setValue(attributeName, normalizeValue)