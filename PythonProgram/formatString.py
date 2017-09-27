age = 24
print("My age is " + str(age) + " years")

print("My age is {0} years".format(age))
# This format is in python3
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(31,
      "Jan", "Mar", "May", "June", "Aug", "Oct", "Dec"))

print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}""".format(28, 30, 31))
#This format is in python2, old format
print("My age is %d years" % age)
print("My age is %d %s, %d, %s" % (age, "years", 6, "months"))

for i in range(1, 11):
    print("No. %2d squared is %4d and cubed is %4d" % (i, i**2, i**3))
for i in range(1, 11):
    print("No. %d squared is %d and cubed is %d" % (i, i**2, i**3))
#12.50f 50 means 50 numbers after decimal point
print("Pi is approximately %12f" % (22/7))
print("Pi is approximately %12.50f" % (22/7))

for i in range(1, 11):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i**2, i**3))
#{*:<*} < means starting from the left side
for i in range(1, 11):
    print("No. {0:<2} squared is {1:<4} and cubed is {2:<4}".format(i, i**2, i**3))

print("Pi is approximately {0:12.50}".format(22/7))