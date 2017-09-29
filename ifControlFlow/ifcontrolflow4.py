print(not True)
print(not False)
age = int(input("How old are you?"))
#if not(age < 18) means if age >= 18
if not(age < 18):
	print("You are old enough to vote")
	print("Please put an X in the bos")
else:
	print("Please come back in {0} years".format(18-age))