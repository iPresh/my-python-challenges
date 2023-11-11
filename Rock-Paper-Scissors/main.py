
import random
from random import seed
from random import randint

print("Welcome to rock, paper, scissors. Good luck!")


user_choice = str(
  input("Please enter your choice: rock, paper, or scissors: ").lower())

possible_actions = ["rock", "paper", "scissors"]
value_for_computer = random.choice(possible_actions)

print(
  f"You chose {user_choice}, while the computer chose {value_for_computer}\n")

if user_choice == "rock" and value_for_computer == "scissors":
  print("Rock smashes Scissors. You win!")

elif user_choice == value_for_computer:
  print("It's a draw!")

elif user_choice == "rock":
  if value_for_computer == "scissors":
    print("Rock smashes Scissors. You win!")
  else:
    print("Paper covers Rock. You lose!")

elif user_choice == "paper":
  if value_for_computer == "rock":
    print("Paper covers Rock. You win!")
  else:
    print("Scissors cut Paper. You lose!")

elif user_choice == "scissors":
  if value_for_computer == "paper":
    print("Scissors cut Paper. You win!")
  else:
    print("Rock smashes Scissors. You lose!")

else:
  print("Please enter a valid choice.")
