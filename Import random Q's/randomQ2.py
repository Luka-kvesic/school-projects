#name       Luka kvesic
#date       2/9/2026
#programme  

import random

userChoice = input("guess if i flip heads or tails, spell heads or tails the same way i do or im not playing: ")

HT = ["heads","tails"]

reality = random.choice(HT)
print("you guessed", userChoice)
print(reality,"was thrown!")
if reality == userChoice:
    print("you win")
else:
    print("you lose")