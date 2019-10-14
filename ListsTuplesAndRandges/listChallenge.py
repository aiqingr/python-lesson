# add to the program below so that if it finds a meal without spam
# it prints out each of the ingredients of the meal
# You will need to set up the menu as did in lines 5-13

menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "bacon", "spam"])

print(menu)

for meal in menu:
    # notice the "not in" syntax
    if not "spam" in meal:
        print(meal)
        for ingredient in meal:
            print(ingredient)
