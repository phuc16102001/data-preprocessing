from Sample import Sample
import math

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
        
    def missingAttribute(self):                            # 1
        result = []
        for attribute in self.lsAttribute:
            for sample in self.data:
                if (sample.getValue(attribute)==""):
                    result.append(attribute)
                    break 
        return result

    def countMissingSample(self):                           # 2
        count = 0
        for sample in self.data:
            if (sample.isMissing()):
                count += 1
        return count

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



    def count(self):
        return len(self.data)
    
    def getSample(self,index):
        return self.data[index]