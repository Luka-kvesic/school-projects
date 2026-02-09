#name       Luka kvesic
#date       2/9/2026
#programme  random guessing game between a hundored

import random #WHOOPS, WILL FIX PROGRAMME SOON, BECUASE THIS IS NOT THE RIGHT ONE

randomNumber = random.randint(1,100)
triesLeft = 7
playing = True
while playing:
    userGuess = int(input("guess a number between 1 and a hundred you have 7 guesses: "))
    if userGuess == randomNumber:
        print("you got it")
        playing = False
    elif userGuess != randomNumber:
        print("try again")
        triesLeft -= 1
    if triesLeft <= 0:
        playing = False
        print("you ran out of guesses")

