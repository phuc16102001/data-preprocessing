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
    Compare two Samples
    
    Args:
        other: the comparing object
    Returns:
        result: a boolean value
    """
    def __eq__(self, other):
        # Must same type
        if (type(self)!=type(other)):
            return False
        
        # Must have same length of attributes
        selfAttr = self.getAttributes()
        otherAttr = other.getAttributes()
        if (len(selfAttr)!=len(otherAttr)):
            return False
        
        # Must have same attributes and values
        for attribute in selfAttr:
            if (not(attribute in otherAttr)):
                return False
            if (self.getValue(attribute)!=other.getValue(attribute)):
                return False
        
        # Pass all condition
        return True
                
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
    
    Returns:
        attributes: a list of String, the list of attributes of Samples (including missing value)
    """
    def getAttributes(self):
        return self.data.keys()
    
    """
    Get the list of missing attribute
    
    Returns:
        missing: the list of attribute whose value is missing
    """
    def getMissing(self):
        missing = []
        for attribute in self.getAttributes():
            if (self.data[attribute]==""):
                missing.append(attribute)
        return missing

    """
    Setter for an attribute
    
    Args:
        attribute: a String represented for the setting attribute
        value: the value to set
    """
    def setValue(self, attribute, value):
        self.data[attribute] = value

    """
    Remove an attribute from a Sample
    
    Args:
        attribute: a String, the attribute name we want to remove
    Returns:
        value: returns the value for that attribute (returns None if not existed)
    """
    def removeAttribute(self, attribute):
        return self.data.pop(attribute,None)

    """
    Override the convert string function
    
    Returns:
        result: an json string represent for a Sample
    """
    def __str__(self):
        return str(self.data)
            