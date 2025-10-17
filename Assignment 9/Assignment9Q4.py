#author: Luka kvesic
#date: 17 october 2025
#description: check how mny times a character is shown
count = 0
character = input("what is the character you want to search for: ")
sentence = input("what is your sentence: ")
sentenceLength = len(sentence)
for i in range(sentenceLength):
    if sentence[i] == character:
        count += 1
print('character',character,'pops up', count,'times')