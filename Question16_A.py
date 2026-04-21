# Question 16(a) 
# Name and School: luka kvesic
import random
Svaccines = ["A","B","C"]
Running = True
while Running:
    s_name = input("Enter your surname: ")
    f_name = input("Enter your first name: ")
    age = int(input("Enter your age: "))
    eircode = input("Enter your Eircode: ")  # K78 E625  #K66 E644
    trial = input("""Do you agree to enrol in a vaccine trial?
type 'Yes' or 'No': """)
    if age < 50:
        vaccine = "MRNA"
    elif age >= 50:
        vaccine = "ADENO"
    lastNum = eircode[-1]
    lastNum = int(lastNum)
    if (lastNum % 2) == 0:
        place = "nothfield"
    elif (lastNum % 2) == 1:
        place  = "Eastwood"

    print("Hello", f_name, s_name,"you are",age,"years old")
    print("you must attend",place,"for your vaccine")
    if trial == "No":
        print(f_name,"you will recieve the",vaccine,"vaccine")
    elif trial == "Yes":
        print("you are enrolled in the trial to recieve Super vaccine",random.choice(Svaccines))
    Q = input("""If you have finished entering peoples details type 'END', otherwise press RETURN: """)
    if Q == "END":
        Running = False


