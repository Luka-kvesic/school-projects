#name       Luka kvesic
#date       2/9/2026
#programme  maths quiz
points = 0
Playing = True
import random
while Playing:
    randomInt1 = random.randint(1,12)
    randomInt2 = random.randint(1,12)
    gamemode = random.randint(1,4)
    if gamemode == 1:
        answer = randomInt1 + randomInt2
        print("the question is", randomInt1, "+", randomInt2 )
        answer = float(answer)
    elif gamemode == 2:
        answer = randomInt1 - randomInt2
        print("the question is", randomInt1, "-", randomInt2 )
        answer = float(answer)
    elif gamemode == 3:
        answer = randomInt1 * randomInt2
        print("the question is", randomInt1, "*", randomInt2 )
        answer = float(answer)
    elif gamemode == 4:
        answer = randomInt1 // randomInt2
        print("the question is", randomInt1, "//", randomInt2 )
        answer = float(answer)
    userAnswer = input("what do you think the answer is: ")
    if userAnswer.isalpha():
        userAnswer = str(userAnswer)
    else:
        userAnswer = float(userAnswer)
    if answer == userAnswer:
        print("thats correct! you get one extra point")
        points += 1
        print()
        print("you now have",points,"points!")
        print()
    else:
        if userAnswer == "q":
            print("bye")
            Playing = False
        else:
            print("thats not the answer, heres another one")
            print()