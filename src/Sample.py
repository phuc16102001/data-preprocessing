class Sample:
    
    data = {}
    
    """
    Initialize for a Sample object
    
    Args:
        attributes: a list of String, the attributes list of the sample
        values: a list of String, the list of each value corresponding to the list attribute
    """
    def __init__(self, attributes, values = []):
        self.data = {}
        for i in range(len(attributes)):
            try:
                self.data[attributes[i]] = float(values[i])
            except:
                self.data[attributes[i]] = values[i]
                
    """
    Get a value corresponding to the attribute
    
    Args:
        attribute: a String, the name of attribute we get
    Returns:
        value: a String or float, the request value
    """
    def getValue(self, attribute):
        return self.data[attribute]
    
    """
    Get the list of attribute of the sample 
    """
    def getAttributes(self):
        return self.data.keys()
    
    def isMissing(self):
        for attribute in self.getAttributes():
            if (self.data[attribute]==""):
                return True
        return False

    def setValue(self, attribute, value):
        self.data[attribute] = value

    def __str__(self):
        return str(self.data)
            