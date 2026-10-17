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
                
                if sentence[i] in """ ,;!?`().:"-'][{}""":
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
    topTen = {}
    wordFrequencyCopy = wordFrequency.copy()
    for key, value in wordFrequency.items():
        highestValue = 0
        for key2, value2 in wordFrequencyCopy.items():
            if value2 > highestValue:
                highestValue = value2
                highestKey = key2
        del wordFrequencyCopy[highestKey]
        topTen[highestKey] = highestValue
    return topTen
                
            


 
file = open("book.txt")
for line in file:
    line = str(line)
    line = line.rstrip("\n")
    wordFrequency = frequencyWords(line)

i = 0

topTen = toptenifier(wordFrequency)
for key, value in topTen.items():
    i += 1
    print(key, value)
    if i == 10:
        break
    
    
