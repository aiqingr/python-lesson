string = "1234567890"
# string and lists are iterable objects

# Actually the for loop handle the error,
# after 0, there is a error, which is no more loop in the for loop, handled by for loop
for char in string:
    print(char)

my_iterator = iter(string)
print(my_iterator)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
# the line 22 will be an error, if we cancel the comment of line 22
# print(next(my_iterator))

for char in iter(string):
    print(char)
