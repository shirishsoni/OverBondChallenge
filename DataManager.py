import pandas as pd

def readInputDataFromCSV(filePath):
    originalInput = pd.read_csv(filePath)
    originalInput['yield'] = originalInput['yield'].map(lambda x: x.rstrip('%')).astype(float)
    originalInput['term'] = originalInput['term'].map(lambda x: x.rstrip('years')).astype(float)
    return originalInput

def getBond(originalInput, type):
    return originalInput[originalInput['type'] == type]