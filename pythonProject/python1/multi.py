def conventer(original_units, coefficient):
    return original_units*coefficient
user_input_1 = int(input("Enter your current units:"))
user_input_2 = int(input("Enter your rate: "))
print(conventer(user_input_1,user_input_2))
