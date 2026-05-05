#Question 16(b)
#Name and School

sentence = input("enter a sentence; ") #this program helps a student keep track of their book club reading list by asking how many books theyve finished reading
vowels = 0
words = 1
for i in range(len(sentence)):
    letter = sentence[i]
    if (letter == "a") or (letter == "o") or (letter == "u") or (letter == "i") or (letter == "e"):
        vowels += 1
    if letter == " ":
        words += 1
print("words: ",words)
print("vowels: ",vowels)