#author: Luka kvesic
#date: 01 september 2025
#description: calculate bill for each person equally
bill = input('how much is the bill: ')
bill = int(bill)
diners = input('how many people are with you: ')
diners = int(diners)
total_bill_forEach = bill / diners
print('the bill will be', total_bill_forEach, 'for each person')