# Question 16(a)
# Name and School: luka kvesic

print("Household budget calculator")
num_adults = int(input("Number of adults in household: "))
num_child = int(input("Number of children in household: "))

food_budget = 300
cost_food_adults = 50
cost_food_child = 35

child_allowance = 140

total_child_allowance = 0
for i in range(num_child):
    if i <= 2:
        total_child_allowance += child_allowance
    elif i > 2:
        total_child_allowance += child_allowance + 20
inflation = float(input("inflation rate (e.g. 0.05 for 5% inflation): "))

totalFoodCost = (cost_food_adults*num_adults+cost_food_child*num_child)*(1+inflation)
print("Children’s allowance total: €", total_child_allowance)
print("Total household food cost: €",round((cost_food_adults*num_adults+cost_food_child*num_child), 2))
print("Total household food cost with inflation: €",round((totalFoodCost), 2))
percentageOnFood = round((totalFoodCost/total_child_allowance) * 100, 2)
print("percentage spend on food:",percentageOnFood,"%")
remaining = round((totalFoodCost)) + total_child_allowance - round((cost_food_adults*num_adults+cost_food_child*num_child), 2)
print("bugdet remaining after food spend: €", remaining)
#im not sure what "food spend" is meant to be