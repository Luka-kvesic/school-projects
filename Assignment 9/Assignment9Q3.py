#author: Luka kvesic
#date: 17 october 2025
#description: change words depeindng o if its consonants and vowels

word = input("what is your word: ")
lengthWord = len(word)
combinedConWord = ""

if word.lower()[0] == 'a' or word.lower()[0] == 'o' or word.lower()[0] == 'i' or word.lower()[0] == 'u' or word.lower()[0] == 'e':
    print(word + "way")

else:
    for letter in range(1, lengthWord):
        letters = word[letter]
        
        combinedConWord += letters
        if letter == lengthWord - 1:
            combinedConWord += word[0]
            combinedConWord += "ay"
    print(combinedConWord)
  