import dayFourData
import json

boards = dayFourData.boards.split('\n\n')

boards = [board.split('\n') for board in boards]

for bn, board in enumerate(boards):
    for bl, nums in enumerate(board):
        stringNums = nums
        stringNums = stringNums.split(' ')
        while "" in stringNums:
            stringNums.remove('')
        stringNums = [int(num) for num in stringNums]
        boards[bn][bl] = stringNums

givenNumbers = dayFourData.numbers.split(',')

givenNumbers = [int(num) for num in givenNumbers]


class bingoBoard:
    def __init__(self, boards : list, numbers : list) -> None:
        self.boards = boards
        self.numbers = numbers
        self.toCall = 0

    def checkWin(self, board : list) -> bool:
        for x in range(0,5):
            # vertical
            if sum([True if board[y][x] == -1 else False for y in range(0, 5)]) == 5:
                return True
            
            # horizontal
            if sum(board[x]) == -5:
                return True
        
        return False
            
    
    def checkBoards(self) -> list:
        for boardNum, board in enumerate(boards):
            for boardList, boardRow in enumerate(board):
                for numIndex, num in enumerate(boardRow):
                    if num == self.numbers[self.toCall]:
                        self.boards[boardNum][boardList][numIndex] = -1
                        if self.checkWin(self.boards[boardNum]):
                            return [True, self.boards[boardNum]]
        
        self.toCall += 1
        return [False]

    def checkBoardsPartTwo(self) -> list:
        toRemove = []
        for boardNum, board in enumerate(boards):
            for boardList, boardRow in enumerate(board):
                for numIndex, num in enumerate(boardRow):
                    if num == self.numbers[self.toCall]:
                        self.boards[boardNum][boardList][numIndex] = -1
                        if self.checkWin(self.boards[boardNum]):
                            toRemove.append(board)
        
        for x in toRemove:
            self.boards.remove(x)
        
        self.toCall += 1
        return [False]

    def calcBoard(self, board : list) -> int:
        total = 0
        
        for x in board:
            for y in x:
                if y > 0:
                    total += y
        
        return total*self.numbers[self.toCall]
                

    def playGame(self) -> int:
        sentinal = [False]
        while len(sentinal) == 1:
            sentinal = self.checkBoards()

        return self.calcBoard(sentinal[1])

    def playGamePartTwo(self) -> int:
        while True:
            self.checkBoardsPartTwo()
            if len(self.boards) == 1:
                break

        self.toCall -= 1

        while self.checkWin(self.boards[0]) == False:
            self.checkBoards()

        print(self.calcBoard(self.boards[0]))
        print(self.numbers[self.toCall])
        for x in self.boards[0]:
            print(x)

        return self.calcBoard(self.boards[0])

partOne = bingoBoard(boards, givenNumbers)

print(partOne.playGamePartTwo())