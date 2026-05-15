alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

possibleToDecrypt = False


def encrypt(string, key):
    index = 50
    encryptedMessage = ""
    for i in range(len(string)):
        index = 50
        letter = string[i]
        if letter in alphabet:
            index = alphabet.index(letter)
        if index != 50:
            letter1 = alphabet[(index + key)%26]
            encryptedMessage += letter1
        elif index == 50:
            encryptedMessage += letter
    return encryptedMessage

def decrypt(string, key):
    index = 50
    decryptedMessage = ""
    for i in range(len(string)):
        index = 50
        letter = string[i]
        if letter in alphabet:
            index = alphabet.index(letter)
        if index != 50:
            letter1 = alphabet[(index - key)%26]
            decryptedMessage += letter1
        elif index == 50:
            decryptedMessage += letter
    return decryptedMessage
string = input("enter a string: ")
stringy = ""
for i in range(len(string)):
    leter = string[i].upper()
    stringy += leter
string = stringy
print("1 is to encrypt 2 is to decrypt")
encry = 1
decry = 2

key = int(input("what is the key: "))

while True:
    answer = int(input("what would you like to do: "))
    if (answer == decry) and (possibleToDecrypt):
        decyptoid = decrypt(encryptoid, key)
        print(encryptoid,"when decrypted with key",key,"turns to",decyptoid)
    elif ((answer == decry) and not (possibleToDecrypt)):
        print("theres nothing to decrypt")
    elif answer == encry:
        encryptoid = encrypt(string, key)
        print("the word",string,"with key",key,"turns to",encryptoid)
        possibleToDecrypt = True

