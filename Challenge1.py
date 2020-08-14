#!/usr/bin/env python

from DataManager import readInputDataFromCSV, getBond


def main():
    # Reading data from CSV and processing it for further computation
    originalInput = readInputDataFromCSV("sample_input.csv")

    # Separating values for corporate and government
    corporateDF = getBond(originalInput, "corporate")
    governmentDF = getBond(originalInput, "government")

    # Generate output
    printOutput(getYield(corporateDF, governmentDF))


def getYield(corporateDF, governmentDF):
    '''
    Used to calculate yield spread for the corporate bonds
    '''
    finalList = []
    for index, row in corporateDF.iterrows():

        intermediateList = []

        for index1, row1 in governmentDF.iterrows():

            temporaryList = []
            temporaryList.append(row['bond'])
            temporaryList.append(row1['bond'])
            temporaryList.append(abs(round(row['term'] - row1['term'], 2)))
            temporaryList.append(round(row['yield'] - row1['yield'], 2))

            # Finding minimum difference of term
            if len(intermediateList) != 0 and temporaryList[2] < intermediateList[0][2]:
                intermediateList = []
                intermediateList.append(temporaryList)

            elif len(intermediateList) == 0:
                intermediateList = []
                intermediateList.append(temporaryList)
        finalList.extend(intermediateList)
    return finalList


def printOutput(finalList):
    print("bond,benchmark,spread_to_benchmark")
    for index1, i in enumerate(finalList):
        print(finalList[index1][0], finalList[index1][1], str(finalList[index1][3]) + "%")


if __name__ == "__main__":
    main()

