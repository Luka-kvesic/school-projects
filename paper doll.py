word = input("enter a word: ")

def paperDoll(word):
    newWord = ""
    for i in range(len(word)):
        
        letter = word[i]
        newWord += letter * 3
    return newWord
string = paperDoll(word)
print(string)