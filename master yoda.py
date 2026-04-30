
sentence = input("enter a sentence: ")

def masterYoda(sentence):
    word = ""
    yodaSentence = ""
    for i in range(1, len(sentence)+ 2):
        print(i)
        letter = sentence[len(sentence)-i]
        if (letter == " ") or (i == len(sentence)+2):
            yodaSentence += word
            word = ""
        word += letter
    return yodaSentence
        
newSentence = masterYoda(sentence)
print(newSentence)