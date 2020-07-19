# Super Mario game made in pyhton


## Description
The game has been programmed in python3 to run on the terminal itself.
Mario is the player, and enemies are generated which move towards mario(left).

Score increases on collecting the coins and landing vertically on the enemies.
Mario has 3 lives, and loses a life on colliding non-vertically with the enemy.

Mario has to reach the castle at the end of the game to win.

## Usage

Install all the requirements using:
```bash
pip install -r requirements.txt
```
Replace the first line of `main.py` with the location of your python installation.
```bash
#!/usr/bin/env python
```
Run the python script
```bash
./main.py
```

## Controls

- Controls follow the tradional classic tiles(W,S,A,D)
- To quit press `Q`

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
