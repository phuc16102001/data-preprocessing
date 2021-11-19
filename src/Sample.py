class Sample:
    
    data = dict()
    
    def __init__(self, attributes, values = []):
        for i in range(len(attributes)):
            try:
                self.data[attributes[i]] = float(values[i])
            except:
                self.data[attributes[i]] = values[i]
                
    def getValue(self, attribute):
        return self.data[attribute]
    
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
            