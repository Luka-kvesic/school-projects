
def frequencyWords(sentence):
    sentence = sentence.lower()
    wordCounter = {}
    evaluatingSentence = True
    i = 0
    while evaluatingSentence:
        word = ""
        evaluatingWord = True
        while evaluatingWord:
            
            if i == len(sentence):
                evaluatingSentence = False
                evaluatingWord = False
                if word in wordCounter:
                    wordCounter[word] += 1
                else:
                    wordCounter[word] = 1
                word = ""
            else:
                
                if sentence[i] == " ":
                    evaluatingWord = False
                    if word in wordCounter:
                        wordCounter[word] += 1
                    else:
                        wordCounter[word] = 1
                    word = ""
                    
                else:
                    word += sentence[i]
            i += 1
    return wordCounter

def frequencyCharacters(sentence):
    sentence = sentence.lower()
    characterCounter = {}
    evaluatingSentence = True
    i = 0
    while evaluatingSentence:
        if i == len(sentence)-1:
            evaluatingSentence = False
            if sentence[i] in characterCounter:
                characterCounter[sentence[i]] += 1
            else:
                characterCounter[sentence[i]] = 1
            break
        if sentence[i] == " ":
            i += 1
            continue
        else:
            if sentence[i] in characterCounter:
                characterCounter[sentence[i]] += 1
            else:
                characterCounter[sentence[i]] = 1
        i += 1
    return characterCounter

trying = True        
while trying:
    option = input("do you want to calculate frequency of words or characters (w/c): ")
    option = option.lower()
    if option == "w":
        sentence = input("enter a sentence: ")
        wordFrequency = frequencyWords(sentence)
        trying = False
        for key, value in wordFrequency.items():
            print(key, value)
    elif option == "c":
        sentence = input("enter a sentence: ")
        characterFrequency = frequencyCharacters(sentence)
        trying = False
        for key, value in characterFrequency.items():
            print(key, value)
    else:
        print("invalid answer, try again")
        trying = True
    
    


#hi hi hi hello hello



