employeeName = input("Employee's Name: ")
numShifts = int(input("Number of shifts: "))
numTransactions = int(input("Number of transactions: "))
transDollarValue = int(input("Transaction dollar value: "))


productivityScore = (transDollarValue / numTransactions) / numShifts

if productivityScore <= 30:
    employeeBonus = 50
elif productivityScore >= 31 and productivityScore <= 69:
    employeeBonus = 75
elif productivityScore >= 70 and productivityScore <= 199:
    employeeBonus = 100
else:
    employeeBonus = 200

print(f"\n\n\nEmployee Name: {employeeName}\n Employee Bonus: {employeeBonus}")