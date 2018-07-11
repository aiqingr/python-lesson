number = [1, 2, 3]
myfile = open("exercise_2.txt", "w")
for i in number:
    myfile.write(str(i) + "\n")
myfile.close()
