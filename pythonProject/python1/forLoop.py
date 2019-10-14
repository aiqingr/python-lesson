myfile = open("fruits.txt")
fruits = myfile.read()
my_fruits = fruits.splitlines()
myfile.close()
for i in my_fruits:
    print(i)
