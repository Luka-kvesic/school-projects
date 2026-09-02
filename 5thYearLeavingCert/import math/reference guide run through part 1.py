#author: Luka kvesic
#date: 2/23/2026
#description: reference guide run through part 1


                      
                            

print("hello this is \n a new line")
print('and he said \'hello\'')
print("and he said \"hello\"")

string = input("give string: ")
print(len(string))

list1 = eval(input("make a list: "))
print(min(list1))
print(max(list1))
print(sum(list1))

list1.clear()
list1.extend(range(0,101,5))
print(list1)

integer = int(input("give number: "))
print(abs(integer))

floaty = float(input("give float: "))
print(round(floaty))

inputy = input("give anything: ")
print(type(inputy))
print(str(12.22))

stringToList = input("give string: ")
print(list(stringToList))

number = input("give something that i can convert to an int without an error: ")
print(int(number))

#the right one will give an error

floatation = float(input(("give something that i can convert to an float without an error: ")))
print(floatation)

aVariable = bool(input("give something and ill check if its true or false: "))
print(aVariable)
print(pow(2,4))
