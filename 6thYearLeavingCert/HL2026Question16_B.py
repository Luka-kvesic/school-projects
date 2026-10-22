

def wordScorer(word):
    errorMsg = "you are only allowed to put letters for one word, try again"
    word = word.upper()
    score = 0
    for letter in word:
        if letter in "AEIOU":
            score += 1
        elif letter in "VWXYZ":
            score += 5
        elif letter in "BCDFGHJKLMNPQRST":
            score += 3
        else:
            return errorMsg
    return score
        


PlayAgain = True
highestScore = 0
while PlayAgain:

    word = input("Enter a word: ")


    score = wordScorer(word)

    if score == "you are only allowed to put letters for one word, try again":
        print(score)
        continue
    else:
        print(word, ": score = ",score)
        repeat = input("Playing again? [Y/N]: ")
        repeat = repeat.upper()
        if score > highestScore:
            highestScore = score
    if repeat == "Y":
        PlayAgain = True
    else:
        PlayAgain = False
        print("Your highest score was ", highestScore)
    
