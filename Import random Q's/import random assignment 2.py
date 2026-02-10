#name       Luka kvesic
#date       2/9/2026
#programme  import random Assignment 2
import random
print("welcome to my dice game!")
name = input("please enter your name: ")
usersLuckyNumber = int(input("please enter a lucky number between 1 and 6: "))
print(name+"'s", "lucky number was: ",usersLuckyNumber)

computerRoll = random.randint(1,6) # initialise computer number
print("the computer rolled: ",computerRoll)

if usersLuckyNumber == computerRoll:
    print("you guessed correctly, well done!")
elif usersLuckyNumber > computerRoll:
    print("you guessed too high")
elif usersLuckyNumber < computerRoll:
    print("you guessed too low")