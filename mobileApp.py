import os
from header import *
import time
import random


#random.seed(time.time())
random.seed(1) #debugging

choice = 0
while(choice != 4):
    choice = int(input("What game would you like to play (1-4): \n1. BattleShip\n2. Connect Four\n3. Tic Tac Toe (2 player)\n4. Exit\n"))
    if(choice == 1):
        size = input("Board size")
        game = battleShip(size)
        game.play()
    if(choice == 2):
        game = connectFour()
        game.printBoard()
    if(choice == 3):
        game = TicTacToe()
        game.play()
    elif(choice == 4):
        continue