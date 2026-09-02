#author: Luka kvesic
#date: 21 october 2025
#description: 7 guesses to guss correct number

correctAnswer = 37
print('i have a number between 1 and a 100 in mind, guess it and you win')

for i in range( 7):
    print('you have', 7-i,'guesses left')

    guess = int(input('enter your guess: '))
    
    if guess == correctAnswer:
        print('you guessed correctly, congrats!')
        break
    elif guess > correctAnswer:
        print('your guess is too high')
    elif guess < correctAnswer:
        print('your guess is too low')
        