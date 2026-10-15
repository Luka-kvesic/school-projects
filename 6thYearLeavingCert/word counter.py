
def countWords(sentence):
    sentence = sentence.upper()
    wordCounter = {}
    evaluatingSentence = True
    i = 0
    while evaluatingSentence:
        word = ""
        evaluatingWord = True
        while evaluatingWord:
            i += 1
            if i == len(sentence):
                evaluatingSentence = False
                evaluatingWord = False
            else:
                if sentence[i] == " ":
                    evaluatingWord = False
                    if word in wordCounter:
                        wordCounter[word] += 1
                    else:
                        wordCounter[word] = 0
                    word = ""
                else:
                    word += sentence[i]
    return wordCounter
    
            


sentence = input("enter a sentence: ")

print(countWords(sentence))


print()