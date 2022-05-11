# Challenge: Rolling Dices

Craps is a game played with a pair of dice. In the game of craps, the shooter (the player with the dice) rolls a pair of dice and the number of spots showing on the two upward faces are added up. If the opening roll (called the 'coming out roll') is a 7 or 11, the shooter wins the game. If the opening roll results in a 2 (snake eyes), 3 or 12 (box cars), the shooter loses, otherwise known as 'crapping out'. If the shooter rolls a 4, 5, 6, 8, 9 or 10 on the opening roll, then he or she must roll the same number before rolling a 7 to win the game. For example, if the shooter rolls a 6 on the come out roll, a 10 on the second roll and a 7 on the third roll, the shooter loses since he rolled a 7 before rolling another 6. If, however, he rolled a 6 on the third roll, he wins the game.

### Requirements

- Python >= 3.9

### Get started

Clone the repository:

    git clone git@github.com:isacaraujo/challenge-rolling-dices.git

Install:

    python -m venv .venv
	source .venv/bin/activate
	pip install -r requirements.txt

Run tests:

    make test
