import random

number = random.randint(1, 11)

attempts = 0

def start_game():
  attempts = 0
  print("Welcome to the Guessing Game!")
  
while True:
  try:
    guess = int(input("Guess: "))
  except ValueError:
    print("Guess with numbers please")  
  if guess > number:
    print("Go lower")
    attempts += 1
  elif guess < number:
    print("Go higher")
    attempts += 1
  elif guess == number:
    break    
print("Got it!")
