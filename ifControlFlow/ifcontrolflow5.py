parrot = "Norwegian Blue"
letter = input("Enter a character: ")
if letter in parrot:
	print("Give me an {}, Bob".format(letter))
else:
	print("I don't need that letter")