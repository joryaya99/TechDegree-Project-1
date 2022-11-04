import random
	
player_score = []
print("Welcome to the Guessing Game!")

def start_game():
	while True:
		number = random.randint(1, 10)
		attempts = 0
	try:
		guess = int(input("Guess: "))
	except ValueError:
		print("Guess with numbers please")
	if guess > 10:
		print("Can't be over 10")
	if guess < 1:
		print("Can't be under 1")
	if guess > number:
		attempts += 1
		print("Go lower")
	if guess < number:
		attempts += 1
		print("Go higher")
	if guess == number:
		attempts +=1
		print("You got it, it took you {} guesses".format(attempts))
		
	player_score.append(attempts)
	player_score.sort()
	break
