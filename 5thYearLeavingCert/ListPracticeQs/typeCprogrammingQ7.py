list1 = []
list2 = []
list3 = []
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in range(50):
    list1.append(i)
    
    
for i in range(1,51):
    num = i ** 2
    list2.append(num)

for i in range(1,26+1):
    list3.append(alphabet[i-1]*i)
print(list1)
print(list2)
print(list3)