for i in range(0,11):
	print("in is now {0}".format(i))

number = "1,231,533,423,423,525,767,964"
cleanedNumber = ""
for i in range(0, len(number)):
	if number[i] in '0123456789':
		print(number[i])

for i in range(0, len(number)):
	if number[i] in '1234567890':
		cleanedNumber = cleanedNumber + number[i]

newNumber = int(cleanedNumber)

print("The new number is {0}".format(newNumber))
print("the new number is {0}".format(int(cleanedNumber)))

for state in ["no pinin", "no more", "a stiff", "bereft of life"]:
	print("This parrot is " + state)
	#print("This parrot is{}".format(state))

for i in range(0, 100, 5):
	print("i is {}".format(i))

for i in range(1, 13):
	for j in range(1, 13):
		print("{1} times {0} is {2}".format(i, j, i*j))
	print("=================")
