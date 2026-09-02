# Question 16(b)
# Name and School: luka kvesic

flight_numbers = eval(input("Enter the flight numebrs: "))
direct = []
indirect = []
for i in range(len(flight_numbers)):
    string = flight_numbers[i]
    string = str(string)
    number = string[-1]
    if number == "2":
        direct.append(flight_numbers[i])
    elif number == "5":
        indirect.append(flight_numbers[i])
print("direct flights are:", direct)
print("indirect flights are:", indirect)   # [122,125,132,135,155]


