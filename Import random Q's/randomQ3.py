#name       Luka kvesic
#date       2/9/2026
#programme  random guessing game heads and tails

import random 

userGuess = input("guess if my coin lands heads or tails, spell your answer the same way i spelt mine or im not playing: ")

options = ["heads", "tails"]

reality = random.choice(options)

print("i landed", reality)
print("you guessed",userGuess)

if userGuess == reality:
    print("you guessed correctly")
else:
    print("you guessed incorrectly")

