# age = int(input("How old are you? "))
# #if 16 <= age <= 65: (this one is also working just as follows)
# if age >= 16 and age <= 65:
# 	print("Have a good day at work")
#
# if age < 16 or age> 65:
# 	print("Enjoy your free time")
# else:
# 	print("Have a good day at work")
#Here x equals a string called "false". The x is not empty or zero
#That is the reason why if statement equals true
x = "false"
if x:
	print("X is true")
print("""false: {0}
None: {1}
0: {2}
0.0: {3}
empty list []: {4}
empty string '': {5}
empty string "": {6}
empty tuple (): {7}
empty mapping: {8}
""".format(False, bool(None), bool(0), bool(0.0),
		   bool([]), bool(''), bool(""), bool(()),
		   bool({})))
print("empty mapping: {0}".format(bool({})))

#, bool(0), bool(0.0), bool([]), bool(''), bool(""), bool(()), bool({})
#empty mapping {}: {8}