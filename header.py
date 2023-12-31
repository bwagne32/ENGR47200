import random
import time

def login(): # This is just here to say we have a login function
    username = input("Hi, what's your name?: \0")
    return username

class battleShip: #=============================================================================
    def __init__(self, size: int):
        self.size: int = size
        self.board = [['O'] * size for _ in range(size)]
        self.firedBoard = [['*'] * size for _ in range(size)]
        for i in range(size):
            randRow = random.randrange(size)
            randCol = random.randrange(size)
            if (self.check(randRow, randCol)):
                self.board[randRow][randCol] = 'X'
            else:
                i -= i
        self.ships = size
            
    def check(self, row: int, column: int):
        return self.board[row][column] == 'O'
    
    def cheatPrintBoard(self): #prints rows x columns for debugging/cheating
        for i in self.board:
            print(" " + str(i))
        print("Ships left: " + str(self.ships))
    
    def printBoard(self):
        for i in self.firedBoard:
            print(" " + str(i))
        print("Ships left: " + str(self.ships))

    def fire(self, row: int, col: int):
        if(self.check(row,col)):
            self.firedBoard[row][col] = 'O'
            print("Miss")
        else:
            print("Hit")
            self.board[row][col] = 'O'
            self.firedBoard[row][col] = 'X'
            self.ships -= 1

    def play(self):
        while(self.ships > 0):
            print("Ships left: " + str(self.ships))
            self.printBoard()
            row: int = int(input("Input row to fire at: (1 - " + str(self.size) + "): "))
            col: int = int(input("Input column to fire at: (1 - " + str(self.size) + "): "))
            if((int(row) > int(self.size)) or (int(col) > int(self.size))):
                print("Out of range")
                continue
        
            self.fire(row - 1, col - 1)
        print("You win!")
        self.printBoard()




# Cut from final game
class connectFour: #=============================================================================
    def __init__(self):
        self.board = [['*'] * 7 for _ in range(6)]

    def printBoard(self):
        for i in range(6):
            print(self.board[i])

    def place(self, col: int):
        for i in range(self.board[0]):
            if(self.board[col][i] == '*'):
                break
            


    def winCheck(self):
        directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
        for row in range(self.rows):
            for col in range(self.columns):
                if self.board[row][col] == " ":
                    continue
                for dr, dc in directions:
                    for _ in range(4):
                        r, c = row + dr * _, col + dc * _
                        if 0 <= r < self.rows and 0 <= c < self.columns and self.board[r][c] == self.board[row][col]:
                            continue
                        break
                    else:
                        return self.board[row][col]
        if self.moves == self.rows * self.columns:
            return "Tie"
        return None

    def play(self):
        print("In process, check back later\n")




class TicTacToe: #=============================================================================
    def __init__(self,bot,piece):
        self.board = [" " for _ in range(9)]  # Create an empty board
        if(piece == 'o' or 'O'):
            self.current_player = 'O'
        else:
            self.current_player = 'X'
        if(bot == 'Y' or 'y'):
            self.bot = 1
        else:
            self.bot = 0

    def print_board(self):
        for i in range(0, 9, 3):
            print(" | ".join(self.board[i:i + 3]))
            if i < 6:
                print("-" * 9)

    def make_move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player
            
            if(not self.bot):
                self.current_player = "X" if self.current_player == "O" else "O"
            else:
                self.current_player = "X" if self.current_player == "O" else "O"
                while " " in self.board:
                    position = random.randrange(1,9)
                    if self.board[position] == " ":
                        self.board[position] = self.current_player
                        break
                self.print_board()
                print("Bot turn")
                self.current_player = "X" if self.current_player == "O" else "O"
                return True
            return True
        else:
            return False

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return self.board[combo[0]]
        if " " not in self.board:
            return "Tie"
        return ""

    def play(self):
        winner = ""
        while winner == "":
            self.print_board()
            try:
                position = int(input(f"Player {self.current_player}, enter your move (1-9): "))
                if position < 1 or position > 9:
                    raise ValueError("Position out of range.")
            except (ValueError, IndexError):
                print("Invalid input. Try again.")
                continue

            if self.make_move(position - 1):
                winner = self.check_winner()
                if winner:
                    self.print_board()
                    if winner == "Tie":
                        print("It's a tie!")
                    else:
                        print(f"Player {winner} wins!")
                    continue