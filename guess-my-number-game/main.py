import random

number = random.randint(1,100)

print("I'm thinking of a number between 1 and 99")
while True:
  user_guess = int(input("Enter your guess: "))

  if user_guess > number:
    print("Too high")
    continue
  elif user_guess < number:
    print("Too low")
    continue
  elif user_guess == number:
    print("Congrats! The number is", number)
    break