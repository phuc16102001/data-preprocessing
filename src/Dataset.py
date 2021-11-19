from Sample import Sample

class Dataset:
    lsAttribute = []
    data = []
    
    def __init__(self, attributes):
        for attribute in attributes:
            self.lsAttribute.append(attribute)
    
    def addSample(self, sample):
        self.data.append(sample)
    
    def addAttribute(self, attributeName, sampleValues):
        self.lsAttribute.append(attributeName)
        for i in range(len(data)):
            self.data[i][attributeName] = sampleValues[i]
        
    def missingAttribute(self):
        result = []
        for attribute in self.lsAttribute:
            for sample in self.data:
                if (sample.getValue(attribute)==""):
                    result.append(attribute)
                    break 
        return result
    
    def countMissingSample(self):
        count = 0
        for sample in self.data:
            if (sample.isMissing()):
                count += 1
        return count
    
    def count(self):
        return len(self.data)
    
    def getSample(self,index):
        return self.data[index]