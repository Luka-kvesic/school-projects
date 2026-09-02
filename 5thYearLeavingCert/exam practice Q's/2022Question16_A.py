#Question 16(a)
# Student name: luka kvesic

print("This programme can find the perimeter or area of a quadrilateral Q")
length = float(input("Please enter the length: "))
witdh = float(input("Please enter the witdh: "))
name = input("please enter your user name: ")
choice = input("Do you want to find the (p)erimeter or (a)rea? ")

if choice == "p":
    print("A quadrilateral with the length of",length,"and width of",witdh,"has a perimeter of",round((length*2) + (witdh * 2),2))
elif choice == "a":
    print("A quadrilateral with the length of",length,"and width of",witdh,"has a area of",round((length * witdh),2))
print("thank you for using the programme", name)
