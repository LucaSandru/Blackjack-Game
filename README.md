# Blackjack Game

This is a simple Blackjack game written in Python. The game allows a user to play against the computer with basic Blackjack rules.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [How to Play](#how-to-play)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/LucaSandru/Blackjack-Game.git
   ```
   
2. Navigate to the project directory:
   ```bash
   cd Blackjack-Game
   ```
   
## Usage
To play the game, simply run the script using Python
```bash
python blackjack.py
```

## Code explanation

### Importing Required Modules
```bash
import random
from os import system, name
```
- **'random'** : this module is used exclusively to import cards from the deck
- **'system'**, **'name'** : These are used to clear the terminal screen (below I will show the function)

### Clear screen function
```bash
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
```
- This function clears the terminal screen. It checks the operating system and uses the appropriate command
- **Observation!** : I have Windows 11 (that's why I used this function to clear terminal)
- If you have mac or linux, [press here](https://www.tutorialspoint.com/how-to-clear-python-shell) to provide same function of _clear()_

### Rest of the functions
- The rest of the functions provided are pretty clear (the name is suggestive)

### Main Loop
- I created a loop just to make this game a lot more fun, for user to play until he/she wants to stop playing by press at the final of the round `n`

## How to play
1. The game will prompt you to play by typing 'y' or 'n'.
2. If you choose to play, you will be asked how much cash you want to spend on the casino.
3. The game will then enter a loop where you can place bets, receive cards, and decide whether to take additional cards or pass.
4. The goal is to get as close to 21 without going over. If you hit 21 exactly with your initial two cards, you get a Blackjack and win immediately
   **Observation**: If you don't know the rules of Blackjack, [click here](docs/blackjack - rules.pdf)
6. The computer will also draw cards, and the game will compare your hand to the computer's hand to determine the winner.
7. After each round, if you still have cash, you can choose to play again or quit.
  
