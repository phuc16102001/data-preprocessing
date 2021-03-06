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
                # Casting for numeric attribute
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
        for attribute in self.getAttributes():
            for sample in self.data:
                value = sample.getValue(attribute)
                if (value==""):
                    # Increase couting of missing attribute (or create in dictionary)
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
            # Get list of missing attribute
            missingAttribute = sample.getMissing()
            if (len(missingAttribute)!=0):
                count += 1
        return count
    
    """
    Get a list of value for an given attribute
    
    Args:
        attribute: a String, name of attribute we want to get
    Returns:
        lsValue: a List of value, values extracted from samples
    """
    def getValues(self, attribute):
        lsValue = []
        for sample in self.data:
            value = sample.getValue(attribute)
            # Skip missing value
            if value == "":
                continue
            lsValue.append(value)
        return lsValue
    
    """
    Fill the missing value of an attribute with methods
    
    Args:
        attributeName: the name of attribute need to fill
        method: the method name (Median, Mode, Mean), the argument is not case-sensitive
    """
    def fillMissingAttribute(self, attributeName, method):
        method = method.upper()
        
        # Extract list values of an attribute
        lsValue = self.getValues(attributeName)
        for value in lsValue:
            if (type(value) == str) and (method!="MODE"):
                raise ValueError("Method for nominal attribute must be method=\"MODE\"")
        
        # Find the filling value (Refers Utils.py)
        fillValue = None
        if method == "MODE":
            fillValue = findMode(lsValue)
        elif method == "MEDIAN":
            fillValue = findMedian(lsValue)
        elif method == "MEAN":
            fillValue = findMean(lsValue)

        # Fill the value to missing one
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
        
        # Extract list values of an attribute
        lsValue = self.getValues(attributeName)
        for value in lsValue:
            if (type(value) == str):
                raise ValueError("You can only normalize for numeric attribute")

        # Calculate all basic property
        minValue = min(lsValue)
        maxValue = max(lsValue)
        mean = findMean(lsValue)
        std = findStd(lsValue)

        # Normalizing
        for sample in self.data:
            value = sample.getValue(attributeName)
            if (value==""):
                continue
            if (method=="MIN-MAX"):
                normalizeValue = normalizeMinMax(minValue, maxValue, value)
            elif (method=="Z-SCORE"):
                normalizeValue = normalizeZScore(mean,std,value)
            sample.setValue(attributeName, normalizeValue)
            
    """
    Remove samples whose number of missing attribute is greater than the threshold
    
    Args:
        threshold: the threshold of missing values to be removed (default is 50%)
    """
    def removeSamples(self, threshold=0.5):
        nAttribute = len(self.getAttributes())
        newData = []
        
        for sample in self.data:
            missingAttribute = sample.getMissing()
            rate = len(missingAttribute)/nAttribute
            
            if (not(rate>threshold)):
                newData.append(sample)
        self.data = newData
        
    """
    Remove attributes whose number of missing samples is greater than the threshold
    
    Args:
        threshold: the threshold of missing samples to be removed (default is 50%)
    """
    def removeAttributes(self, threshold=0.5):
        missingAttribute = self.missingAttribute()
        nSample = self.count()
        
        for attribute in missingAttribute.keys():
            rate = missingAttribute[attribute]/nSample
            
            # Skip if rate is not larger than threshold
            if (rate<=threshold):
                continue
            
            # Remove attribute
            self.lsAttribute.remove(attribute)
            for sample in self.data:
                sample.removeAttribute(attribute)
            
    """
    Remove duplicated samples
    """
    def removeDuplicated(self):
        newData = []
        for sample in self.data:
            # Compare with __eq__ method which is overrided
            if (not(sample in newData)):
                newData.append(sample)
        self.data = newData
        
    """
    Add a new attribute with expression
    
    Args:
        expression: a String, the expression for new attribute
    """
    def addAttributeExpression(self, expression):
        self.lsAttribute.append(expression)
        for sample in self.data:
            sample.setValueExpression(expression)