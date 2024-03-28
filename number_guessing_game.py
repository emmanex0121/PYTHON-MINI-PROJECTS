#!/usr/bin/env python3
# This program generates a random number between 1 and user_input
# and asks user to guess them

from random import randint
print("############### WELCOME TO THE GUESSING GAME ################\n")

print("#####################    HOW TO PLAY    #####################")
print("# Provide the Upper Bound number you want to guess from\
        \n# The Game Generates a number from 1 to the number provided\
        \n# You can now guess the number the game generates\
        \n# If you are wrong, the game hints you whether your guess\
        \n# is above or below the Real Number\n")

while True:
    user_number = input("Type a number: ")
    if user_number in ('exit', 'EXIT'):
        exit(0)

    if user_number.isdigit():
        user_number = int(user_number)
        break
    else:
        print("\t\tINVALID ENTRY!\n\t\tPlease Enter a Number")
        continue

random_number = randint(1, user_number)

# user_guess = input("Guess the number: ")

number_guesses = 0
while True:
    user_guess = input("Guess the number: ")
    if user_guess in ('exit', 'EXIT'):
        exit(0)

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("\t\tINVALID ENTRY!\n\t\tPlease Enter a Number")
        continue

    if user_guess <= 0 or user_guess > user_number:
        msg = "\t\tOUT OF BOUNDS!\n\t\tPlease enter a number between 1 and "
        print(msg, user_number)
        continue
    else:
        number_guesses += 1
        if user_guess == random_number:
            print("\t\tGREAT! You got it right!")
            break
        else:
            if user_guess > random_number:
                print("INCORRECT - above number, Try again!\n")
            elif user_guess < random_number:
                print("INCORRECT - below number, Try again!\n")
        continue

print("\t\tYou got it in ", number_guesses, "guesses")
