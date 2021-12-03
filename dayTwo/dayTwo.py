import dayTwoData

data = dayTwoData.data.splitlines()

class drive():

    def __init__(self) -> None:
        self.horizontal = 0
        self.vertical = 0
        self.aim = 0

    def move(self, direction : str, magnitude : int):
        if direction == "forward":
            self.horizontal += magnitude
        elif direction == "down":
            self.vertical += magnitude
        elif direction == "up":
            self.vertical -= magnitude

    def splitString(self, string : str):
        split = string.split(' ')
        return [split[0], int(split[1])]

    def move2(self, direction : str, magnitude : int):
        if direction == "forward":
            self.horizontal += magnitude
            self.vertical += self.aim * magnitude
        elif direction == "down":
            self.aim += magnitude
        elif direction == "up":
            self.aim -= magnitude


x = drive()


for a in data:
    b = x.splitString(a)
    x.move2(b[0], b[1])

print(x.horizontal, x.vertical)
print(x.horizontal * x.vertical)