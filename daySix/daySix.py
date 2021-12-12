from daySixData import data
from collections import defaultdict

data = data.split(',')

for i in range(0, len(data)):
    data[i] = int(data[i])

class birthCycle:
    def __init__(self, startingData : list) -> None:
        self.fishList = startingData
        self.fishDic = self.listToDic(self.fishList)

    def listToDic(self, inList : list) -> defaultdict:
        toReturn = defaultdict(lambda : 0)

        for x in inList:
            toReturn[x] += 1

        return toReturn

    def processDay(self, dicToProcces : defaultdict) -> defaultdict:
        emptyDic = defaultdict(lambda : 0)

        for key in dicToProcces.keys():
            value = dicToProcces[key]

            if key == 0:
                emptyDic[6] += value
                emptyDic[8] += value

            else:
                emptyDic[key-1] += value

        return emptyDic

    def goThroughDays(self, numOfDays : int) -> int:

        for x in range(0, numOfDays):
            self.fishDic = self.processDay(self.fishDic)

        return sum([x for x in self.fishDic.values()])

partOneTest = birthCycle(data)

print(partOneTest.fishDic)

print(partOneTest.goThroughDays(80))