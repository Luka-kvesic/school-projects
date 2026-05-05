# Question 16(a)
# Name and School:

books = []
num = int(input("How many books have you read? "))
for i in range(num):
    books.append(input("enter the title of the book you have read: "))

if num >= 3:
    print("fantastic! you have read",num,"books - keep reading!")
print("Book(s) read:")
for i in range(num):
    print(books[i])