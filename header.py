import random
import time


class battleShip:
    def __init__(self, size: int):
        self._size: int = size
        self._board = [['O'] * size for _ in range(size)]
        for i in range(size):
            randRow = random.randrange(size)
            randCol = random.randrange(size)
            if (self.check(randRow, randCol)):
                self._board[randRow][randCol] = 'X'
            else:
                i -= i
        self._ships = size
            
    def check(self, row: int, column: int):
        return self._board[row][column] == 'O'
    
    def printBoard(self): #prints rows x columns for debugging/cheating
        for i in self._board:
            print(" " + str(i))
        print("Ships left: " + str(self._ships))
    
    def fire(self, row: int, col: int):
        if(self.check(row,col)):
            print("Miss")
        else:
            print("Hit")
            self._board[row][col] = 'O'
            self._ships -= 1

    def game(self):
        while(self._ships > 0):
            print("Ships left: " + str(self._ships))
            self.printBoard()
            row: int = input("Input row to fire at: (1 - " + str(self._size) + "): ")
            col: int = input("Input column to fire at: (1 - " + str(self._size) + "): ")
            row: int = int(row)
            col: int = int(col)
            if((int(row) > int(self._size)) or (int(col) > int(self._size))):
                print("Out of range")
                continue
            #try:
            self.fire(row - 1, col - 1)
            #except:
            #    print("Only input integers less than " + str(self._size + 1))
        print("You win!")