# Question 16 (a)
# Name and School:luka kvesic

flight_num = input("Enter your flight number: ")
destination = input("Enter your destination: ")
num_ppl = int(input("Enter the number of people in the travel group: "))
num_children = int(input("Enter the number of children in the travel group: "))

two_letters = flight_num[0:2]
three_numbers = flight_num[2:5]
letters = ""
for i in range(2):
    letters += two_letters[i].upper()
flight_num = letters + three_numbers
if flight_num == "EI121":
    cost = 520
elif flight_num == "EI125":
    cost = 400
    
    
print("There are ",num_ppl,"people in your travel group")
print("you are travelling to",destination)
print("your flight number is",flight_num)
print("The total cost of your flights is",chr(0x20ac),(cost*num_ppl)-(num_children * 50))

#EI121
#orlando
#7

