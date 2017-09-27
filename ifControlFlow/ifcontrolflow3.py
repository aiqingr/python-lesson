print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess != 5:
	if guess > 5:
		print("Please guess lower")
	else:
		print("Please guess higher")

	guess = int(input())
	if guess != 5:
		print("Sorry, you have not guessed correctly")
	else:
		print("Well done, you guess it")
else:
	print("You got it first time")