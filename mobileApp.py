import os
from header import *
import time
import random

random.seed()
#random.seed(1) #debugging

username = login()
print("Hi, " + username + "\n")

choice = 0
while(choice != 4):
    choice = int(input("1. BattleShip (1 player)\n"
                       "2. Connect Four (Cut from final project)\n"
                       "3. Tic Tac Toe\n"
                       "4. Exit\n"
                       + username + ", what game would you like to play (1-4): \0"))
    if(choice == 1):
        size = int(input("Board size: "))
        game = battleShip(size)
        game.play()
    if(choice == 2):
        game = connectFour()
        choice = 4
        break
        #game.cheatPrintBoard()
        game.printBoard()
        game.play()
    if(choice == 3):
        game = TicTacToe(input("Singleplayer? (y/n): "),input("Select X or O?: "))
        game.play()
    elif(choice == 4):
        continue