# Please enter name:
print("******************")
print("* Conversions *")
print("******************")
print("1) From teaspoons to ml")
print("2) From tablespoons to ml")
print("3) From cups to ml")
print("4) From ml to teaspoons")
print("5) From ml to tablespoons")
print("6) From ml to cups")
conversion = int(input("Please enter the conversion, for example: enter '1' if you wish to convert teaspoons to ml:"))
if conversion == 1:
    teaspoons = float(input("Please enter number of teaspoons:"))
    ml = teaspoons * 5
    print("The ml is:", ml)
elif conversion == 2:
    tablespoons = float(input("Please enter number of tablespoons:"))
    ml = tablespoons * 15
    print("The ml is:", ml)
elif conversion == 3:
    cups = float(input("Please enter number of cups:"))
    ml = cups * 4*60
    print("The ml is:", ml)
elif conversion == 4:
    ml = float(input("Please enter number of ml for teaspoons:"))
    teaspoons = ml / 5
    print("The teaspoons is:", teaspoons)
elif conversion == 5:
    ml = float(input("Please enter number of ml for tablespoons:"))
    tablespoons = ml / 15
    print("The tablespoons is:", tablespoons)
elif conversion == 6:
    ml = float(input("Please enter number of ml for cups:"))
    cups = ml / (60*4)
    print("The cups is:", cups)
