num = [1,2,3,2]
denum = [2,1,4,7]
preFraction = 0
for i in range(len(num)):
    fraction = num[i] / denum[i]
    if i == 0:
        preFraction = fraction
    if fraction < preFraction:
        preFraction = fraction
        frac = str(num[i]) + "/" + str(denum[i])
        iSaved = i
print(frac,"is smallest at index:", iSaved)