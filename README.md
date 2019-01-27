## Super Mario game made in pyhton

- Author: Akshay Kharbanda

The game has been implemented using python3 on the terminal display.
Mario is the player, and enemies are generated which move towards mario(left).

Score is increased on collecting the coins and landing vertically on the enemies.
Mario has 3 lives, and loses a life on colliding non-vertically with the enemy.

Mario has to reach the castle at the end of the game to win.

All objects including the board are colored for a better playing experience and bonus marks.

## Structure

The application demonstrates inheritance, encapsulation, polymorphism as well as overloading.
- Each object is derived from the "Object" class
- The board has its own class and captures all objects placed on it.

## Running the program

- First, install all the requirements :
		- 'pip install -r requirements.txt'
- Now simply replace the first line of "main.py" with the location of your python installation
		-  #!/usr/bin/env python
- Running the main program is easy
		- ./main.py

## Controls

- Controls follow the tradional classic tiles(W,S,A,D)
- To quit press 'q'

## Scoring

- 50 points for capturing a coin
- 100 points for killing an enemy

## Symbols

-   $$
	||  --> Mario

-   bb
	bb  --> Brick

-   EE
	EE  --> Enemy

-   O   --> Coin
