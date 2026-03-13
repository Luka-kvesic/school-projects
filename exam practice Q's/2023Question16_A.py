#Question 16(a)
#Write your name here: luka kvesic
option = input("would you like to (a)dd, (s)ubtract, (m)ultiply or (d)ivide?")
num1 = float(input("please enter your first number: "))
num2 = float(input("please neter your second number: "))
if option == "a":
    print(num1,"+",num2,"=",round(num1 + num2,2))
if option == "s":
    print(num1,"-",num2,"=",round(num1 - num2,2))
if option == "m":
    print(num1,"*",num2,"=",round(num1 * num2,2))
if option == "d":
    print(num1,"/",num2,"=",round(num1 / num2,2))
