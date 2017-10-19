fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}
# there is no error in the console if we have duplicate key, however
# there will be a warning
# "apple": "round and crunchy"
# print(fruit)
# print(fruit["lime"])
# fruit["pear"] = "an odd shaped apple"
print(fruit)
# fruit["pear"] = "great with tequila"
# print(fruit)
# del fruit["lime"]
# print(fruit["lime"])
# del fruit
# fruit.clear()
# print(fruit)
# print(fruit["tomato"])
# print(fruit)
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key, "We don't have a " + dict_key)
#     print(description)
# if dict_key in fruit:
#     description = fruit.get(dict_key)
#     print(description)
# else:
#     print("We don't have that fruit")
# for snack in fruit:
#     print(fruit[snack])
#
# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print("-" * 48)
# Dictionary is not ordered. So if we want to print the values ordered, we need
# to ordered the keys first.
ordered_key = list(fruit.keys())
ordered_key.sort()
# ordered_key = sorted(list(fruit.keys()))
for f in ordered_key:
    print(f + " - " + fruit[f])
