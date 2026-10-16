wordCounter = {}
print("\"")
def frequencyWords(sentence):
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
                
                if sentence[i] == " " or (sentence[i] == "\""):
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













file = open("book.txt")
for line in file:
    
    wordFrequency = frequencyWords(line)
print(wordFrequency)