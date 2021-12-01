import dayOneData

data = dayOneData.data.split(', ')

class dayOne:

   def __init__(self):
      self.position = [0,0] # x, y
      self.angle = 90
   
   def parseInstruc(self, instru : str):
      if instru[0] == "L": self.angle += 90
      else: self.angle -= 90
      
      if self.angle < 0: self.angle = 270
      elif self.angle > 270: self.angle = 0

      distance = int(instru[1:])

      if self.angle == 0: self.position[0] += distance
      elif self.angle == 90: self.position[1] += distance
      elif self.angle == 180: self.position[0] -= distance
      elif self.angle == 270: self.position[1] -= distance

start = dayOne()

for x in data:
   start.parseInstruc(x)

print(start.position[0] + start.position[1])




      