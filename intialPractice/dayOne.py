
import dayOneData

data = dayOneData.data.split(', ')

class dayOne:

   def __init__(self):
      self.position = [0,0] # x, y
      self.angle = 90
      self.locationsBeen = [[0,0]]
      self.index = 1
   
   def parseInstruc(self, instru : str):
      if instru[0] == "L": self.angle += 90
      else: self.angle -= 90
      
      if self.angle < 0: self.angle = 270
      elif self.angle > 270: self.angle = 0

      distance = int(instru[1:])

      prevLoca = self.locationsBeen[i-1]

      if self.angle in [0, 180]:
         toAdd = [[x, self.position[1]] for x in range(prevLoca[0], )]

      if self.angle == 0: self.position[0] += distance
      elif self.angle == 90: self.position[1] += distance
      elif self.angle == 180: self.position[0] -= distance
      elif self.angle == 270: self.position[1] -= distance

      self.index += 1


   def getPosition(self):
      return [self.position[0], self.position[1]]
      

start = dayOne()

givenCord = [[0,0]]

for z in data:
   start.parseInstruc(z)
   currentPos = start.getPosition()
   if currentPos in givenCord:
      break
   else:
      givenCord.append(currentPos)
      index = givenCord.index(currentPos)
      if givenCord[index-1][0] != currentPos[0]:
         toAdd = [[x, currentPos[1]] for x in range(givenCord[index-1][0], currentPos)]
         for x in toAdd:
            givenCord.append()
     

print(sum(currentPos))


"""
position = [0, 0]
angle1 = 90

def parseInstruc(instru : str):
   global angle1, position
   if instru[0] == "L": angle1 += 90
   else: angle1 -= 90
   
   if angle1 < 0: angle1 = 270
   elif angle1 > 270: angle1 = 0

   distance = int(instru[1:])

   if angle1 == 0: position[0] += distance
   elif angle1 == 90: position[1] += distance
   elif angle1 == 180: position[0] -= distance
   elif angle1 == 270: position[1] -= distance


def getPosition():
   return [position[0], position[1]]


u = []
for x in data:
   parseInstruc(x)
   u.append(getPosition())
print(u)

for i, x in u:
   for j, y in u:
      if x == y:
         print(x)
         break


"""