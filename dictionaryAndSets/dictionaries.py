fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}
# there is no error in the console if we have duplicate key, however
# there will be a warning
# "apple": "round and crunchy"
print(fruit)
print(fruit["lime"])
fruit["pear"] = "an odd shaped apple"
print(fruit)
fruit["pear"] = "great with tequila"
print(fruit)
# del fruit["lime"]
# print(fruit["lime"])
# del fruit
# fruit.clear()
# print(fruit)
# print(fruit["tomato"])
print(fruit)
while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    if dict_key in fruit:
        description = fruit.get(dict_key)
        print(description)
    else:
        print("We don't have that fruit")
