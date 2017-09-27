name = input("Please enter your name: ")
#please notice the next line, the int make the age as an integer
#this can make ">=" symbol working, ">=" can work only between two numbers

age = int(input("How old are you, {0}?".format(name)))
print(age)
if age >= 18:
	print("You are old enough to vote")
	print("Please put an X in the bos")
else:
	print("Please come back in {0} years".format(18 - age))

