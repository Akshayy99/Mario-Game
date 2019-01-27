'''
Contains the board class along with the methods and other features
'''
import sys
import os
from os import system
import time
import random
from objects import *
import config

rows = 60
cols = 200
start = 0
end = 200
columns = 100000
grid = []
init_x = 53
init_y = 10
mario = Mario(init_x, init_y)

for i in range(rows-5):
    grid.append(['\x1b[6;30;44m'+' '+'\x1b[0m'] * columns)

for i in range(5):
    grid.append(['\x1b[6;30;42m'+'T'+'\x1b[0m'] * columns)

bricks = []
for i in range(10):
    for j in range(5):
        brick = Brick(49, 70*(i+1)+2*j)
        bricks.append(brick)

x = random.randint(start, end)

enemies = []
for i in range(20):
    enemies.append(Enemy(53, random.randint(35, 1200)))

coins = []
for i in range(20):
    coins.append(Coin(47, random.randint(25, 2000)))
    coins.append(Coin(45, random.randint(25, 2000)))
    coins.append(Coin(43, random.randint(25, 2000)))
    coins.append(Coin(41, random.randint(25, 2000)))

pipes = []
for i in range(0, 1500):
    if i % 70 == 0:
        pipes.append(Pipe(52, i))
    if i % 100 == 0:
        pipes.append(Pipe(52, i))


class Board():
    def __init__(self):
        self.score = 0
        self.won = False
        self.lost = False

    def process_input(self, player, key_press):
        '''# to process the key press and take according action'''
        global start
        global end
        res = False
        if key_press in config.DIR:
            x, y = player.get_coords()
            # inverted up down calc because of top left origin
            if key_press == config.UP:
                player.isJump()
                return
            elif key_press == config.LEFT:
                if y >= start+2:
                    y -= config.x_fac
            elif key_press == config.RIGHT:
                if y < (start+end)/2:
                    y += config.x_fac
                else:
                    start += 1
                    end += 1

            res = self.update_location(player, x, y)

        return res

    def check(self):
        if end == 400:
            return -1
        return 1

    def lost(self):
        x = int((start+end)/2)
        for i in range(len(config.lost)):
            for j in range(len(config.lost[0])):
                grid[75+i][x+j] = config.lost[i][j]
        time.sleep(5)

    def insert(self):
        listt = []
        clouds = []
        for i in range(start, end):
            if i % 40 == 0:
                listt.append(i)
        for i in listt:
            clouds.append(Cloudd(i, 20))
        for cloud in clouds:
            self.printCloud(cloud)

        for enemy in enemies:
            enemy.draw(grid)

        for brick in bricks:
            brick.draw(grid)

        for coin in coins:
            coin.draw(grid)
        for pipe in pipes:
            pipe.draw(grid)

        for i in range(len(config.castle)):
            for j in range(len(config.castle[0])):
                grid[43+i][300+j] = config.castle[i][j]

        for i in range(len(config.won)):
            for j in range(len(config.won[0])):
                grid[10+i][255+j] = config.won[i][j]

    def printCloud(self, cloud):

        i, p = cloud.getCoords()
        ln = 5
        lnn = 8
        for j in range(lnn):
            for k in range(ln):
                grid[k+2][i+j] = cloud.structure[k][j]

    def collisionME(self):
        global mario
        global enemies
        global score
        mx, my = mario.get_coords()
        for enemy in enemies:
            x, y = enemy.getCoords()
            if mx+2 == x and my == y or mx+2 == x and my == y+1 or mx+2 == x and my == y-1:
                enemies.remove(enemy)
                self.score += 100
            if mx == x and my == y-1 or mx == x and my == y+1:
                mario.lives -= 1

    def collisionMB(self,player):
        mx, my = player.get_coords()
        jumpinit = mx
        for brick in bricks:
            x, y = brick.getCoords()
            # if collision on top
            if mx+2 == x and my == y or mx+2 == x and my+1 == y or mx+2 == x and my == y+1:
                player.toJump = False

            # if empty space below
            if grid[mx+2][my] == '\x1b[6;30;44m'+' '+'\x1b[0m' and grid[mx+2][my+1] == '\x1b[6;30;44m'+' '+'\x1b[0m' and player.toJump == False:
                player.toJump = True
                player.jumpinit = 49
                player.var = 53

            # if colliding from below, rebound
            if mx == x+2 and my == y or mx == x+2 and my+1 == y or mx == x+2 and my == y+1:
                player.toJump = True
                player.var += 4

    def collisionMC(self, player):
        global score
        mx, my = player.get_coords()
        for coin in coins:
            x, y = coin.getCoords()
            if mx == x and my == y or mx+1 == x and my == y or mx+1 == x and my+1 == y or mx+1 == mx and my == y+1:
                coins.remove(coin)
                self.score += 50

    def collisionMP(self, player):
        mx, my = player.get_coords()
        jumpinit = mx

        for pipe in pipes:
            x, y = pipe.getCoords()

            if mx+1 == x and my == y or mx+1 == x and my+1 == y or mx+1 == x and my == y+1 or mx+1 == x and my == y+2  or mx+1 == x and my == y+3 or mx+2 == x and my == y or mx+2 == x and my+1 == y or mx+2 == x and my == y+1 or mx+2 == x and my == y+2  or mx+2 == x and my == y+3:
                player.toJump = False

            if grid[mx+2][my] == ' ' and grid[mx+2][my+1] == ' ' and player.toJump == False:
                player.toJump = True
                player.jumpinit = 49
                player.var = 53

            if mx == x+1 and my == y-1:
                player._x = mx

    def draw(self, player):
        player._x, player._y = player.get_coords()

        if player._x < 1200:
            tmp = player.structure
            grid[player._x][player._y] = tmp
            for i in range(2):
                for j in range(2):
                    grid[player._x+i][player._y+j] = tmp[i][j]

    def clear(self, obj):
        x, y = obj.get_coords()
        for i in range(2):
            for j in range(2):
                try:
                    grid[x+i][y+j] = '\x1b[6;30;44m'+' '+'\x1b[0m'
                except:
                    pass

    def update_location(self, player, new_x, new_y):
        '''update location of mario'''
        self.clear(player)

        player._x, player._y = new_x, new_y

        self.draw(player)

    def render(self, player):
        ''' displaying the board at every frame'''
        # os.system('clear')        
        # system("tput reset")
        global score
        print('Super Mario Bros     ||      Lives: {}           '.format(player.lives), end = '')
        print('Score:  {}'.format(self.score))

        if player.toJump:
            player.jump(self)
        
        self.insert()
        
        print("\x1b[{};{}H".format(0,0))
        for i in range(rows):
            for j in range(start, end):
                print(grid[i][j], end='')
            print('')
