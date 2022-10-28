import random

player_score = []
print("Welcome to the Guessing Game!")

def start_game():
	number = random.randint(1, 11)
	attempts = 0

while True:
  try:
    guess = int(input("Guess: "))
  except ValueError:
    print("Guess with numbers please")
		continue
	if guess > 10:
		print("Can't be over 10")
		continue
	if user_guess < 1:
		print("Can't be under 1")
		continue
  if guess > number:
    print("Go lower")
    attempts += 1
  if guess < number:
    print("Go higher")
    attempts += 1
  elif guess == number:
		attempts +=1
		print("You got it, it took you {} guesses".format(attempts))
		player_score.append(attempts)
		player_score.sort()
    break
