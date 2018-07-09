temp = [10,-20,-289,100]
def c_to_f(c):
    if c < -273.15:
        print("Temprature can not be less than 273.15 Celsius")
    else:
        return c*9/5+32

for i in temp:
    print(c_to_f(i))
