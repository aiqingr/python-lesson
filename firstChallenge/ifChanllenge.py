#Write a small program to ask for a name and an age.
#With both values have been entered, check if the person
#is the right age to go on an 18-30 holiday (they must be
#over 18 and under 31).
#a (polite) message refusing them entry.
print("Please enter your name: ")
name = input()
print("Please enter your age: ")
age = int(input())
if 18 < age < 31:
	print("Happy Holiday.")
else:
	print("Hi {0}, You are not qualified to have the holiday".format(name))