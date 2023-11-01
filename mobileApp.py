import os
from header import *
import time
import random


#random.seed(time.time())
random.seed(1) #debugging

choice = 0
while(choice != 4):
    choice = int(input("1. BattleShip\n"
                       "2. Connect Four\n"
                       "3. Tic Tac Toe (2 player)\n"
                       "4. Exit\n"
                       "What game would you like to play (1-4): \0"))
    if(choice == 1):
        size = input("Board size: ")
        game = battleShip(size)
        game.play()
    if(choice == 2):
        game = connectFour()
        game.printBoard()
        game.play()
    if(choice == 3):
        game = TicTacToe()
        game.play()
    elif(choice == 4):
        continue