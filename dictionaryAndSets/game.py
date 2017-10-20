# Modify the program so that the exits is a dictionary rather than a list,
# with the keys being the numbers of he locations and the values being
# dictionaries holding the exits (as they do at present). No change should
# be needed to the actual code.
#
# Once that is working, create another dictionary that contains words that
# players may use. These words will be the keys, and their values will be
# a single letter that the program can use to determine which way to go.

locations = {0: "you are sitting in froint of a computer learning python",
             1: "You are sitting at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a small house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

nameExits = {1: {"2": 2, "3": 3, "4": 4, "5": 5},
             2: {"5": 5},
             3: {"1": 1},
             4: {"1": 1, "2": 2},
             5: {"2": 2, "1": 1}}

vocabulary = {"QUIT": "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST": "E",
              "WEST": "W",
              "ROAD": "1",
              "HILL": "2",
              "BUILDING": "3",
              "VALLEY": "4",
              "FOREST": "5"}

# print(locations[0].split())
# print(locations[3].split())
loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break
    else:
        allExits = exits[loc].copy()
        allExits.update(nameExits[loc])
    direction = input("Available exists are " + availableExits).upper()
    print()
    # Parse the user input, using our vocabulary dictionary if necessary
    if len(direction) > 1:  # More than one letter
        words = direction.split()
        for word in words:     # Does it contain a word we know
            if word in vocabulary:
                direction = vocabulary[word]

    if direction in allExits:
        loc = allExits[direction]
    else:
        print("You cannot go in that direction")