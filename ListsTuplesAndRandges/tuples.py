# Including the parentheses or not, depend on yourself.
# Recommend to use parentheses.
# Such as e(line 7)
# Tuples are immutable.
# t = "a", "b", "c"
# print(t)
#
# e = ("a", "b", "c")
# print(e)
#
# print("a", "b", "c")
# print(("a", "b", "c"))

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad company", "Bad company", 1974
budgie = "Nightflight", "budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lighting", "Metallica", 1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])
# Tuples are immutable, however, it can be reassigned.
# Notice the line 26 and the rest of codes
# metallica[0] = "Master fo puppets"
imelda = imelda[0], "Imelda May", imelda[2]
print(imelda)

metallica2 = ["Ride the Lighting", "Metallia", 1983]
print(metallica2)
metallica2[0] = "Master of Puppets"
metallica2[2] = "hello world"
print(metallica2)