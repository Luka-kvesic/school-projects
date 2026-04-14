#Question16_A_OL
#Name; luka kvesic

print("welcome to the Step Tracker app!")
name = input("please enter your name: ")
steps_today = int(input("Enter the number of steps you walked today: "))
if steps_today >= 10000:
    print("well done",name," youve reached your goal")
elif steps_today < 0:
    print("the number of steps cant be negative")
elif steps_today <= 5000:
    print("Aim to do more steps today!",name)
elif (steps_today >= 5000) and (steps_today <= 9999):
    print("Good effort",name, " almost there!")
    
    