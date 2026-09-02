#Question 16(b)
# Student name: luka kvesic


import random

computer_options = ["rock","paper","scissors"]
player_choice = input("please enter rock, paper or scissors: ")
print("player chose:",player_choice)
computer_choice = computer_options[(random.randint(0,2))]
print("computer chose", computer_choice)

if computer_choice == "rock":
    if player_choice == "paper":
        print("player wins!")
    elif player_choice == "rock":
        print("draw")
    elif player_choice == "scissors":
        print("computer wins!")
elif computer_choice == "scissors":
    if player_choice == "paper":
        print("computer wins!")
    elif player_choice == "rock":
        print("player wins!")
    elif player_choice == "scissors":
        print("draw!")
elif computer_choice == "paper":
    if player_choice == "paper":
        print("draw!")
    elif player_choice == "rock":
        print("computer wins!")
    elif player_choice == "scissors":
        print("player wins!")
