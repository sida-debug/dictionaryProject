def get_stats(animals):
    dataList = []
    animalList = []
    ageDict = {}
    weightDict = {}
    lengthDict = {}
    countDict = {}
    for i in range (len(animals)):
        dataList.append(animals[i].split(","))

    for i in range (len(dataList)):
        if dataList[i][0] not in animalList:
            animalList.append(dataList[i][0])

    def averageDictMaker(whichDict, j):
        for i in range(len(dataList)):
            if dataList[i][0] not in whichDict:
                whichDict[dataList[i][0]] = [int(dataList[i][j])]
            else:
                whichDict[dataList[i][0]].append(int(dataList[i][j]))
        for i in animalList:
            whichDict[i] = round((sum(whichDict[i]))/(len(whichDict[i])), 1)
            whichDict[i] = str(whichDict[i])
        return whichDict

    ageDict = averageDictMaker(ageDict, 1)
    weightDict = averageDictMaker(weightDict, 2)
    lengthDict = averageDictMaker(lengthDict, 3)

    for i in range(len(dataList)):
        if dataList[i][0] not in countDict:
            countDict[dataList[i][0]] = 1
        else:
            countDict[dataList[i][0]] +=1

    print(animals)
    print(dataList)
    print(animalList)
    print(ageDict)
    print(weightDict)
    print(lengthDict)
    print(countDict)
    print("\n")

    finalStr = ""
    for i in animalList:
        finalStr+= i
        finalStr += ", "
        finalStr += str(countDict[i])
        finalStr += ", "
        finalStr += ageDict[i]
        finalStr += ", "
        finalStr += weightDict[i]
        finalStr += ", "
        finalStr += lengthDict[i]
        finalStr = finalStr + "\n"
    return finalStr

print(get_stats(["hamster,1,7,5", "alligator,9,13,12", "hamster,4,8,6", "cat,13,12, 9", "snake,14,11,8", "cat,10,8,9", "hamster,1,10,5", "cat,4,14,6", "snake,7,11,6","alligator,7,14,5"]))