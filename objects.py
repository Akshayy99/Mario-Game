'''
contains the structure of each person
'''
import sys
import os
import random
import config
import time
from board import *

class Object():
	def __init__(self, x, y):
		self._x = x
		self._y = y 
		self.structure = []

	def getStruct(self):
		return self.structure

	def getCoords(self):
		return (self._x, self._y)


class Cloudd(Object):
	def __init__(self, x, y):
		super(Cloudd, self).__init__(x, y)
		self.structure.append(['\x1b[4;30;44m'+' '+'\x1b[0m','\x1b[4;30;44m'+' '+'\x1b[0m','\x1b[4;30;44m'+' '+'\x1b[0m','\x1b[4;30;44m'+'_'+'\x1b[0m','\x1b[4;30;44m'+' '+'\x1b[0m','\x1b[4;30;44m'+' '+'\x1b[0m','\x1b[4;30;44m'+' '+'\x1b[0m','\x1b[4;30;44m'+' '+'\x1b[0m'])
		self.structure.append(['\x1b[4;30;44m'+' '+'\x1b[0m','\x1b[4;30;44m'+'_'+'\x1b[0m','\x1b[4;30;44m'+'('+'\x1b[0m','\x1b[4;30;44m'+' '+'\x1b[0m','\x1b[4;30;44m'+')'+'\x1b[0m','\x1b[4;30;44m'+'_'+'\x1b[0m','\x1b[4;30;44m'+'_'+'\x1b[0m','\x1b[4;30;44m'+' '+'\x1b[0m'])
		self.structure.append(['\x1b[4;30;44m'+'('+'\x1b[0m','\x1b[4;30;44m'+' '+'\x1b[0m','\x1b[4;30;44m'+' '+'\x1b[0m','\x1b[4;30;44m'+' '+'\x1b[0m','\x1b[4;30;44m'+' '+'\x1b[0m','\x1b[4;30;44m'+' '+'\x1b[0m','\x1b[4;30;44m'+' '+'\x1b[0m','\x1b[4;30;44m'+')'+'\x1b[0m'])
		self.structure.append(['\x1b[4;30;44m'+' '+'\x1b[0m','\x1b[4;30;44m'+'('+'\x1b[0m','\x1b[4;30;44m'+' '+'\x1b[0m','\x1b[4;30;44m'+' '+'\x1b[0m','\x1b[4;30;44m'+' '+'\x1b[0m','\x1b[4;30;44m'+' '+'\x1b[0m','\x1b[4;30;44m'+')'+'\x1b[0m','\x1b[4;30;44m'+' '+'\x1b[0m'])
		self.structure.append(['\x1b[4;30;44m'+' '+'\x1b[0m','\x1b[4;30;44m'+' '+'\x1b[0m','\x1b[4;30;44m'+'('+'\x1b[0m','\x1b[4;30;44m'+'_'+'\x1b[0m','\x1b[4;30;44m'+'_'+'\x1b[0m','\x1b[4;30;44m'+')'+'\x1b[0m','\x1b[4;30;44m'+' '+'\x1b[0m','\x1b[4;30;44m'+' '+'\x1b[0m'])
		self.type = "Cloud"


class Mario():
	def __init__(self, x_pos, y_pos):
		self._x = x_pos
		self._y = y_pos
		self.structure = []
		self.structure.append(['\x1b[1;31;43m'+'$'+'\x1b[0m','\x1b[1;31;43m'+'$'+'\x1b[0m'])
		self.structure.append(['\x1b[6;30;47m'+'/'+'\x1b[0m','\x1b[6;30;47m'+'\\'+'\x1b[0m'])
		self.lives = 3
		self.type = "Mario"
		self.height = 2
		self.width = 2
		self.toJump = False
		self.var = 0
		self.jumpinit = 0

	def isJump(self):
		if self.toJump == True:
			return 
		self.toJump = True
		self.var = self._x
		self.jumpinit = self._x

	def jump(self, board):
		self.var += 1
		board.clear(self)

		if self.toJump and self.var - self.jumpinit > 0 and self.var - self.jumpinit <= 4:
			self._x -= config.y_fac
			board.draw(self)
		elif self.toJump and self.var - self.jumpinit >= 5 and self.var - self.jumpinit <= 8:
			self._x += config.y_fac
			if self._x > 53:
				self._x = 53
				self.toJump = False
				self.var = 0
				self.jumpinit = self._x

			board.draw(self)
		else:
			self.var = 0
			self.toJump = False
			self._x = self.jumpinit

	def get_coords(self):
		''' returns (x, y)'''
		return (self._x, self._y)

	def get_type(self):
		'''returns whether "Mario", "Cloud", "Enemy", etc'''
		return self._type

	def get_size(self):
		return (self.height, self.width)
		
	def update_coords(self, x, y):
		self._x += x
		self._y += y


class Enemy(Object):
	def __init__(self, x, y):
		super(Enemy, self).__init__(x, y)

	def draw(self, grid):

		x, y = self.getCoords()
		for i in range(2):
			for j in range(2):
				try:
					grid[x+i][y+j] = '\x1b[6;30;44m'+' '+'\x1b[0m'
				except:
					pass
		self._y -= 3
		x, y = self.getCoords()
		grid[x][y] = '\x1b[1;30;47m'+'E'+'\x1b[0m'
		grid[x][y+1] = '\x1b[1;30;47m'+'E'+'\x1b[0m'
		grid[x+1][y] = '\x1b[1;30;47m'+'E'+'\x1b[0m'
		grid[x+1][y+1] = '\x1b[1;30;47m'+'E'+'\x1b[0m'


class Brick(Object):
	def __init__(self, x, y):
		super().__init__(x, y)

	def draw(self, grid):
		x, y = self.getCoords()
		grid[x][y] = '\x1b[6;30;41m'+'b'+'\x1b[0m'
		grid[x][y+1] = '\x1b[6;30;41m'+'b'+'\x1b[0m'
		grid[x+1][y] = '\x1b[6;30;41m'+'b'+'\x1b[0m'
		grid[x+1][y+1] = '\x1b[6;30;41m'+'b'+'\x1b[0m'


class Coin(Object):
	def __init__(self, x, y):
		super().__init__(x, y)

	def draw(self, grid):
		x, y = self.getCoords()
		grid[x][y] = '\x1b[6;37;43m'+'O'+'\x1b[0m'


class Pipe(Object):
	def __init__(self, x, y):
		super().__init__(x, y)

	def draw(self, grid):
		x, y = self.getCoords()
		grid[x][y] = '\x1b[0;30;45m'+'T'+'\x1b[0m'
		grid[x][y+1] = '\x1b[0;30;45m'+'T'+'\x1b[0m'
		grid[x][y+2] = '\x1b[0;30;45m'+'T'+'\x1b[0m'
		grid[x+1][y] = '\x1b[0;30;45m'+'|'+'\x1b[0m'
		grid[x+1][y+1] = '\x1b[0;30;45m'+'|'+'\x1b[0m'
		grid[x+1][y+2] = '\x1b[0;30;45m'+'|'+'\x1b[0m'
		grid[x+2][y] = '\x1b[0;30;45m'+'|'+'\x1b[0m'
		grid[x+2][y+1] = '\x1b[0;30;45m'+'|'+'\x1b[0m'
		grid[x+2][y+2] = '\x1b[0;30;45m'+'|'+'\x1b[0m'
