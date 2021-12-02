import day5Data

class day5():

   def __init__(self, data = ""):
      data.replace('\n', '')
      self.data = list(data)
        

   def checkSame(self, one, two):
      if (one.lower() == two.lower() and two != one): 
         return True
      else:
         return False

   def setData(self, data:str):
      data.replace('\n', '')
      self.data = list(data)

   def partOne(self):
      x = 0
      while x < len(self.data)-1:
         if self.checkSame(self.data[x], self.data[x+1]):
            self.data.pop(x+1)
            self.data.pop(x)
            if x > 0: x -= 1

         else: 
            x += 1
         

   def returnLen(self):
      return len(self.data)

   def check(self):
      for x in range(1, len(self.data)-1):
         if self.checkSame(self.data[x], self.data[x+1]):
            print('bad')

test = day5(day5Data.data)
test.partOne()

print(test.returnLen())
print(test.checkSame('a', 'A'))
test.check()
#print(test.data)

