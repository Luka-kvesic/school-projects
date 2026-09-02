#author: luka kvesic
#Date: 01/02/2026
#programme: hangman
import random

print("Welcome to hangman. please save a life guessing the correct word.")
hangManStages = ['''





''','''

|  
| 
|  
|
''','''
+--
|  
| 
|  
|
''',''' 
+--\               
|         
|          
|          
|                
''','''
+--\                
|  ()
| 
|  
|
''','''
+--\                   
|  ()
|  []             
|  
|
''','''
+--\                      
|  ()
| /[]              
|  
|
''','''
+--\               
|  ()
| /[]\                 
|  
|
''','''
+--\                  
|  ()
| /[]\                
|  ]
|
''','''
+--\                 
|  ()
| /[]\                   
|  ][
|
''']


possibleWords = ["words","hang","man","guess","correct"]

word = random.choice(possibleWords)
guessStateString = ""
guess = 0
tries = 0
guessedLetters = []
correctGuesses = 0
necasarycorrectGuesses = len(word)
guessState = []
guessedCorrectly = False
letterDupe = False
for i in range(len(word)):
    guessState.append("-")
Playing = True
restart = False
while Playing:
    if restart:
        word = possibleWords[random.randint(0,4)]
        guessStateString = ""
        guess = 0
        tries = 0
        guessedLetters = []
        correctGuesses = 0
        necasarycorrectGuesses = len(word)
        guessState = []
        guessedCorrectly = False
        letterDupe = False
        for i in range(len(word)):
            guessState.append("-")
        restart = False
    print("-------","try:",tries,"-------")
    print(hangManStages[tries])
    if tries == len(hangManStages)-1:
        print("we lost a good man...")
        decision = input("would you like to play again, yes or no:")
        if decision == "no":
            print("bye")
            Playing = False
            break
        elif decision == "yes":
            restart = True
            continue
    
    
    guessStateString = ""
    for i in range(len(guessState)):
        guessStateString += guessState[i]
    print('Guess the Word:',guessStateString)
    guess = input("enter a character: ")
    for i in range(len(guessedLetters)):
        if guess == guessedLetters[i]:
            letterDupe = True
            
    if letterDupe != True:
        for i in range(len(word)):
            if guess == word[i]:
                correctGuesses += 1
                if correctGuesses == necasarycorrectGuesses:
                    print("you got it, he's saved! the word was:",word)
                    decision = input("would you like to play again, yes or no:")
                    if decision == "no":
                        print("bye")
                        Playing = False
                        break
                    elif decision == "yes":
                        restart = True
                        continue
                else:
                    guessState.pop(i)
                    guessState.insert(i,guess)
                    guessedCorrectly = True
    else:
        print("you already tried that one")
    if (Playing) and (not restart) and (not letterDupe):
        if guessedCorrectly:
            print("you got a letter!")
            guessedCorrectly = False
        else:
            print("thats not one, tough luck")
            tries += 1
    letterDupe = False
    guessedLetters.append(guess)
                    
        
    
    
    


