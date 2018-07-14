correct_password = "python123"
name = input("Enter name: ")
surname = input("Enter Surname: ")
password = input("Enter password: ")

while correct_password != password:
    password = input("Wrong password! Enter again: ")

# print("Hi", name, "you are logged in!")
# print("Hi %s %s you are logged in!" % (name, surname))
message = "Hi %s %s you are logged in!" % (name, surname)
print(message)
