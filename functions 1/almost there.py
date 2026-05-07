
distance = int(input("how far are we: "))

def almostThere(distance):
    if ((distance >= 90) and (distance <= 110)) or ((distance >= 190) and (distance <= 210)):
        return True
    else:
        return False

answer = almostThere(distance)
print(answer)
