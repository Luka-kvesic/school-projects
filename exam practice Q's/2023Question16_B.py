#Question 16(b)
#Write your name here: luka kvesic

import random
words = ["cat","mat","can","man","pool","tool","mule","pat","tan","rule"]
print("the list of words is",words)
random_words = words[random.randint(0,len(words)-1)]


length = len(random_words)
print("the length of the word is:",length)
print("the first letter of the word is:",random_words[0])
guesses = 3
Playing = True
while Playing:
    if guesses == 0:
        print("the word was", random_words)
        Playing = False
        continue
    guess = input("please guess what the word is: ")
    if guess != random_words:
        print("you guesses incorrectly, try again")
    elif guess == random_words:
        print("you guessed correctly!")
        print("the word was", random_words)
        Playing = False
    guesses -= 1
