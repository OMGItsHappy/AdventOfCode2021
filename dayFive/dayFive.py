import dayFiveData
        
from collections import defaultdict

data = dayFiveData.data

data = data.splitlines()

data = [cords.split(' -> ') for cords in data]

class cordPair:
    def __init__(self, startX : int, startY : int, endX : int, endY : int) -> None:
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY
        self.isDiag = startX != endX and startY != endY
        self.pointsList = self.pointList()

    def pointList(self):
        if self.isDiag:
            x, y = -1 if self.startX > self.endX else 1, -1 if self.startY > self.endY else 1

            xList = [xVal for xVal in range(self.startX, self.endX + x, x)]
            yList = [yVal for yVal in range(self.startY, self.endY + y, y)]

            return [[xList[x], yList[x]] for x in range(0, len(xList))]


        elif self.startY != self.endY:
            if (self.startY > self.endY):
                start = self.endY
                end = self.startY
            else:
                start = self.startY
                end = self.endY

            return [[self.startX, x] for x in range(start, end + 1)]

        else:
            start = self.startX
            end = self.endX

            if self.startX > self.endX :
                start = self.endX
                end = self.startX

            return [[x, self.startY] for x in range(start, end + 1)]

listOfPoints = defaultdict(lambda : 0)

def partOne(inputList):

    notDiagList = []

    for i, cordPairs in enumerate(inputList):
        startX, startY = cordPairs[0].split(',')
        endX, endY = cordPairs[1].split(',')

        temp = cordPair(int(startX), int(startY), int(endX), int(endY))
        if not temp.isDiag: notDiagList.append(temp)

    for cords in notDiagList:
        for cord in cords.pointsList:
            listOfPoints[str(cord)] += 1

    print(sum([1 if x[1] > 1 else 0 for x in listOfPoints.items()]))

def partTwo(inputList):
    for i, cordPairs in enumerate(inputList):
        startX, startY = cordPairs[0].split(',')
        endX, endY = cordPairs[1].split(',')

        inputList[i] = cordPair(int(startX), int(startY), int(endX), int(endY))
        

    for cords in inputList:
        for cord in cords.pointsList:
            listOfPoints[str(cord)] += 1
            if cords.startX == 8 and cords.startY == 0: print(cords.pointsList)

    print(sum([1 if x[1] > 1 else 0 for x in listOfPoints.items()]))

partTwo(data)