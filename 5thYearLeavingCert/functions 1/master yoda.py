
sentence = input("enter a sentence: ")

def masterYoda(sentence):
    word = ""
    yodaSentence = ""
    for i in range(0, len(sentence)+1):
        print(i)
        reversedWord = ""
        letter = sentence[len(sentence)-(i+1)]
        if (letter == " ") or (i == len(sentence)):
            for i in range(len(word)):
                reversedWord += word[len(word)-(i+1)]
            reversedWord += " "
            yodaSentence += reversedWord
            word = ""
            reversedWord = ""
        else:
            word += letter
    return yodaSentence
        
newSentence = masterYoda(sentence)
print(newSentence)
