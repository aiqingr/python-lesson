correct_password = "python123"
name = input("Enter name: ")
password = input("Enter password: ")

while correct_password != password:
    password = input("Wrong password! Enter again: ")

# print("Hi", name, "you are logged in!")
print("Hi %s you are logged in!" % name)
