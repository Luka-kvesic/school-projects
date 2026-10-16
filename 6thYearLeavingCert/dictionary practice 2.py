wordCounter = {}
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
                    if word != "":
                        wordCounter[word] = 1
                word = ""
            else:
                
                if sentence[i] in """ ,;!?`().:"-][{}""":
                    evaluatingWord = False
                    if word in wordCounter:
                        wordCounter[word] += 1
                    else:
                        if word != "":
                            wordCounter[word] = 1
                    word = ""
                    
                else:
                    word += sentence[i]
            i += 1
    return wordCounter



def toptenifier(wordFrequency):
    



file = open("book.txt")
for line in file:
    line = str(line)
    line = line.rstrip("\n")
    wordFrequency = frequencyWords(line)



topTen = toptenifier(wordFrequency)

for key, value in wordFrequency.items():
    print(key, value)
    
    
