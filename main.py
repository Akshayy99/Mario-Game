import os
import sys
import random
import time
from board import *
from objects import *
from config import *

board = Board()
var = True

def main():
	while(var):
		if(mario.lives == 0):
			print('Game Over!!')
			time.sleep(2)
			break
		board.render(mario)
		p_input = config.get_key(config.get_input())
		if p_input == config.QUIT:
			break
		board.process_input(mario, p_input)
		board.collisionME()
		board.collisionMB(mario)
		board.collisionMC(mario)
		board.collisionMP(mario)
		if board.check == -1:
			break
		


if __name__ == '__main__':
	main()