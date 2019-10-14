def calculate_age(year):
    age = 2018 -year
    return age

user_input = int(input("Enter your birth year: "))
print(calculate_age(user_input))
