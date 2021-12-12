from daySevenData import data

data = [int(x) for x in data.split(',')]

class moveClass:
    def __init__(self, inList : list) -> None:
        self.horizontalList = self.sortList(inList)
        self.maxVal = self.horizontalList[-1]
        self.unsorted = inList
        
    def minHorizontal(self) -> int:
        vals = []
        nums = 0
        #print(self.maxVal)
        for i in range(0, self.maxVal+1):
            #print(i)
            for x in self.unsorted:
                nums += abs(x-i)
            vals.append(nums)
            print(nums, i)
            nums = 0
        
        b = self.sortList(vals)
        vals.sort()
        print(b)
        return b[0]

    def sumFactorial(self, num : int) -> int:
        total = 0

        for x in range(0, num+1):
            total += x
        
        return total

    def recursiveFactorial(self, num : int) -> int:
        if num == 1:
            return 1
        else:
            return num + self.recursiveFactorial(num-1)


    def sortList(self, inList : list) -> list:
        for initialPoint in range(0, len(inList)-1):
            smallest = initialPoint
            for nextPoint in range(initialPoint, len(inList)):
                if(inList[nextPoint] > inList[smallest] ):
                    smallest = nextPoint
            inList[nextPoint], inList[smallest] = inList[smallest], inList[nextPoint]
        
        return inList

    def findMedian(self) -> int:
        #return self.horizontalList[int(len(self.horizontalList)/2)] if len(self.horizontalList)%2 != 0 else sum(self.horizontalList(self.horizontalList)/2 - 1:len(self.horizontalList)/2

        if (len(self.horizontalList) % 2 == 0):
            x = int(len(self.horizontalList)/2)
            y = int(x-1)
            return (self.horizontalList[x]+self.horizontalList[y])/2
        else:
            return self.horizontalList[int(len(self.horizontalList)/2)]
    

    def minHorizontal2(self) -> int:
        vals = []
        nums = 0
        #print(self.maxVal)
        for i in range(0, self.maxVal+1):
            #print(i)
            for x in self.unsorted:
                nums += self.sumFactorial(abs(x-i))
            vals.append(nums)
            nums = 0
        
        b = self.sortList(vals)
        vals.sort()
        print(b)
        return b[0]


test = moveClass(data)

assert(test.sumFactorial(10) == test.recursiveFactorial(10))
#print(test.minHorizontal())
print(test.minHorizontal2())
