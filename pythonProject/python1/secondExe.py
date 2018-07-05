def conventer(CDegree):
    f = CDegree*9/5 + 32
    return f
user_input = float(input("Enter you temperature with Celsius: "))
if user_input < -273.15:
    print("The lowest temperature is -273.15")
else:
    print(conventer(user_input))
