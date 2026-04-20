# Question 16 (a)
# Name and School:luka kvesic

flight_num = input("Enter your flight number: ")
destination = input("Enter your destination: ")
num_ppl = int(input("Enter the number of people in the travel group: "))
print("your flight number is",flight_num)
print("you are travelling to",destination)
print("There are ",num_ppl,"people in your travel group")
if flight_num == "EI121":
    cost = 520
elif flight_num == "EI125":
    cost = 400
print("The total cost of your flights is",chr(0x20ac),cost*num_ppl)

#EI121
#orlando
#7

