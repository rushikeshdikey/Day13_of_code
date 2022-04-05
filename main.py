# start to python day-13 code
# starting code is basics learned
# main project code at end

# Author: Rushikesh Dikey
# Date: 01-03-2022

import random
import os
from time import sleep
# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
screen_clear()

############Scope#############

# Local scope

# def runs_scored():
#    runs = 15
#    print(f"Inside fun{runs}")
#
# runs_scored()
# #print(f"Outside fun{runs}")
#
# # Global scope
#
# runs = 10
#
# def runs_scored():
#    runs_total = 15
#    print(f"Inside fun{runs}")
#
# runs_scored()
# print(f"Outside fun{runs}")
#
# # Global constant
# PI = 3.14159
#
# def pie():
#    print(PI)
#
# pie()
import random

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 to 100.")

EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5

answer = random.randint(1, 100)
attempt = 0
should_continue = True

# while should_continue:
level = input("Choose a difficulty, Type 'easy' or 'hard': ").lower()

def dificulty():
   if level == 'easy':
      turn = EASY_LEVEL_TURN
      attempt = 10
      print(f"You have {attempt} attempts remaining to guess the number.")
   elif level == 'hard':
      turn = HARD_LEVEL_TURN
      attempt = 5
      print(f"You have {attempt} attempts remaining to guess the number.")
   else:
      return "Invalid difficulty level"

def compare_number(answer, guess):
   if answer > guess:
      print("Too Low")
   elif answer < guess:
      print("Too High")
   else:
      print(f"You guess it right, correct number is {answer}")
while should_continue:

   dificulty(level)
   guess = int(input("Make a guess:"))
   compare_number(answer, guess)
# print(random_number())
