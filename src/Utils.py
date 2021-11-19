import math

"""
Find the mode value of a list

Args:
    lsValue: the list of value
Returns:
    result: the mode value
"""
def findMode(lsValue):
    frequency = {}
    for value in lsValue:
        if (value in frequency):
            frequency[value] += 1
        else:
            frequency[value] = 1
    result = max(frequency, key=frequency.get)
    return result

"""
Find the median value of a list

Args:
    lsValue: the list of value
Returns:
    result: the median value
"""
def findMedian(lsValue):
    lsValue.sort()
    mid = len(lsValue)//2
    
    result = lsValue[mid]
    if (len(lsValue)%2 == 0):
        result = (lsValue[mid] + lsValue[mid+1])/2
    return result

"""
Find the mean value of a list

Args:
    lsValue: the list of value
Returns:
    result: the mean value
"""
def findMean(lsValue):
    total = 0
    for value in lsValue:
        total += value
    result = total / len(lsValue)
    return result

"""
Find the standard deviation (std)

Args: 
    lsValue: the list of value
Returns:
    result: the std value
"""
def findStd(lsValue):
    std = 0
    mean = findMean(lsValue)
    for value in lsValue:
        std += (value-mean)**2
    std = math.sqrt(std/len(lsValue))
    return std

"""
Normalize the value using min-max method

Args: 
    minValue: the minimum value
    maxValue: the maximum value
    value: the normalizing value
Returns:
    normalizeValue: the value after normalized
"""
def normalizeMinMax(minValue,maxValue,value):
    normalizeValue = (value-minValue)/(maxValue-minValue)
    return normalizeValue

"""
Normalize the value using z-score method

Args: 
    mean: the mean value of the list
    std: the std value of the list
    value: the normalizing value
Returns:
    normalizeValue: the value after normalized
"""
def normalizeZScore(mean, std, value):
    normalizeValue = (value-mean)/std
    return normalizeValue