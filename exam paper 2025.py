#Question 16(a)
#Name and School: luka kvesic

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit,2)
def fahrenheit_to_celsius(fahrenheit):
    celsius = (5/9) * (fahrenheit - 32)
    return round(celsius,2)
answer = int(input("Enter 1 for celcius to fahrenheit conversion or 2 for fahrenheit to celcius conversion : "))

if answer == 1:    #conditional
    celsius = float(input("Enter the tempature in celsius: "))
    print(celsius,chr(176),"C is equal to",celsius_to_fahrenheit(celsius),chr(176),"F and ",round(celsius + 273.15,2),"K")
if answer == 2:    #conditional
    fahrenheit = float(input("Enter the tempature in fahrenheit: "))
    print(fahrenheit,chr(176),"F is equal to",fahrenheit_to_celsius(fahrenheit),chr(176),"C and ",round(fahrenheit_to_celsius(fahrenheit) + 273.15,2),"K")


