from DataManager import readInputDataFromCSV, getBond


def main():
    # Reading data from CSV and processing it for further computation
    originalInput = readInputDataFromCSV("sample_input.csv")

    corporateDF = getBond(originalInput, "corporate")
    governmentDF = getBond(originalInput, "government").sort_values(by=['term'])

    governmentList = governmentDF.values.tolist()

    # Generating output
    printOutput(getYieldSpreadToCurve(corporateDF, governmentList))


def getYieldSpreadToCurve(corporateDF, governmentList):
    finalList = []
    for index, row in corporateDF.iterrows():
        for i in range(len(governmentList)):
            if row['term'] < governmentList[i][2]:
                temporaryList = []
                previousIndex = i - 1
                interpolatedValue = interpolateYield(governmentList[previousIndex][3], governmentList[i][3],
                                                     governmentList[previousIndex][2], governmentList[i][2],
                                                     row['term'])
                spreadToCurve = round(row['yield'] - interpolatedValue, 2)
                temporaryList.append(row['bond'])
                temporaryList.append(spreadToCurve)
                break
        finalList.append(temporaryList)

    return finalList


def printOutput(finalList):
    print("bond,spread_to_curve")

    for index1, i in enumerate(finalList):
        print(finalList[index1][0], str(finalList[index1][1]) + "%")


def interpolateYield(gYield1, gYield2, gTerm1, gTerm2, cTerm):
    slope = (gYield2 - gYield1) / (gTerm2 - gTerm1)
    return round(slope * (cTerm - gTerm1) + gYield1, 2)


if __name__ == "__main__":
    main()

