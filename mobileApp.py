import os
from header import *
import time
import random


#random.seed(time.time())
random.seed(1) #debugging

game = 0
while(game != 4):
    game = int(input("What game would you like to play (1-4): \n1. BattleShip\n2. Connect Four\n3. Tic Tac Toe\n4. Exit\n"))
    if(game == 1):
        size = input("Board size")
        ship = battleShip(size)
        ship.game()
    elif(game == 4):
        break