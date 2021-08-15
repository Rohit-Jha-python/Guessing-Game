# Using while loop and random function
import random

attempts = 5
highest = 50
answer = random.randint(1, highest)
# print(answer)

print("WELCOME TO THE NUMBER GUESSING GAME")
print("*" * 40)
print("Rules :\n1. Guess the correct number within the range in {} attempts. \n2. Enter '0' to Quit "
      "the Game.".format(attempts))
print("*" * 40)
name = input("Please Enter Your Name to Begin: ")
while not name.isalpha():
    name = input("Invalid Name, Please Enter Your Name Again:")

print()

guess = 0
count = 0
print("\nHello {}, Guess a number between 1 to {}: ".format(name, highest))
while guess != answer:
    guess = int(input())
    count += 1
    if count == attempts and guess != answer:  # Player gets only 5 guesses to make.
        print("\nYou had enough chances to guess, the correct number was {}.".format(answer))
        break
    elif guess == answer:
        print("\nWell Done {}, you guessed it correctly, the number is {} !!!".format(name, answer))
        print("It took you {} attempts to guess the right number.".format(count))
        break
    elif guess > highest:
        print("Invalid Input, Please select a number within range 1 to {} !!!".format(highest))
    elif guess == 0:
        print("Ok {}, you are allowed to quit the game.".format(name))
        break
    elif guess < answer:
        if count == attempts - 1:
            print("Please Guess Higher, This is Your Last Attempt !!!")
        else:
            print("Please Guess Higher !!!")
    elif count == attempts - 1:
        print("Please Guess Lower, This is Your Last Attempt !!!")
    else:
        print("Please Guess Lower !!!")

