import os
from header import *
import time
import random


#random.seed(time.time())
random.seed(1) #debugging
username = input("Hi, what's your name?: \0")

choice = 0
while(choice != 4):
    choice = int(input("Hi, " + username + "\n"
                       "1. BattleShip\n"
                       "2. Connect Four\n"
                       "3. Tic Tac Toe (2 player)\n"
                       "4. Exit\n"
                       + username + 
                       ", what game would you like to play (1-4): \0"))
    if(choice == 1):
        size = int(input("Board size: "))
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