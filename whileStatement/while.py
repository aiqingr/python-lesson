# for i in range(10):
#     print("i is {} now".format(i))
#
# j = 0
# while j < 10:
#     print("j is {} now".format(j))
#     j += 1
#
# available_exit = ["East", "North", "West"]
# chosen_exit = ""
# while chosen_exit not in available_exit:
#     chosen_exit = input("Please choose a direction: ")
#     if chosen_exit == "quit":
#         print("Game over")
#         break
#
# else:
#     print("Aren't you glad you got out of there!")

import random
highest = 10
answer = random.randint(1, highest)
# print(answer)
print("Please guess a number between 1 and {} ".format(highest))
guess = int(input())
if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you haven;t guessed correctly")
else:
    print("You got it first time")
