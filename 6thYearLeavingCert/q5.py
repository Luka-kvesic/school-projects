



def reciprofyer(number):
    if number == 0:
        return 0
    else:
        return 1/number + reciprofyer(number-1)






number = int(input("enter a number: "))

reciprocal = reciprofyer(number)

print(reciprocal)