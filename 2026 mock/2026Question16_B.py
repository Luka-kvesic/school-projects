#Question16_B_OL
#Name; luka kvesic

print("welcome to my weekly step tracker!")
monday = int(input("please enter the number of steps you took on monday: "))
tuesday = int(input("please enter the number of steps you took on tuesday: "))
wednesday = int(input("please enter the number of steps you took on wednesday: "))
thursday = int(input("please enter the number of steps you took on thursday: "))
friday = int(input("please enter the number of steps you took on friday: "))
saturday = int(input("please enter the number of steps you took on saturday: "))
sunday = int(input("please enter the number of steps you took on sunday: "))

weeksSteps = [monday,tuesday,wednesday,thursday,friday,saturday,sunday]

print("the list of steps taken is:",weeksSteps)
total = monday + tuesday + wednesday + thursday + friday + saturday + sunday
print("the total number of stepstaken this week is", total)
average = total / 7
average = round(average,2)
print("the average number of steps taken is ",average)

highest = 0
savedHighest = 0

for i in range(7):
    if weeksSteps[i] > savedHighest:
        savedHighest = weeksSteps[i]
print("the largest number of steps you took this week is",savedHighest)

lowest = 999999999999999999999999999999999
for i in range(7):
    if weeksSteps[i] < lowest:
        lowest = weeksSteps[i]
print("the lowest number of steps you took this week is",lowest)
    
    
