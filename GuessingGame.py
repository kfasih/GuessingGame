#!/usr/bin/env python3
# author: kdfasih

# This application generates a number between 1 and 10 (inclusive).
# The user is asked to make a guess within this range. If the guess
# is too low, the application will let the user know to guess higher.
# If the user's guess is too high, the application will tell them to guess
# a lower number. If the user guesses correctly, they are congratulated
# and asked if they want to play again.

import random

def playGame():
    randomValue = int(random.randint(1, 10))
    guess = None
    print('Guess a number between 1 and 10')
    while (True):
        guess = int(input())
        if (guess < randomValue):
            print('Too low, try again: ')
        elif (guess > randomValue):
            print('Too high, try again: ')
        else:
            print('Nice, you didn\'t waste my time')
            print('The correct value was {}'.format(randomValue))
            playAgain = input('Play Again? ')
            if (playAgain == 'yes'):
                randomValue = random.randint(1, 10)
                print('Guess a number between 1 and 10')
                guess = None
            else:
                print('Thanks for playing')
                break

playGame()