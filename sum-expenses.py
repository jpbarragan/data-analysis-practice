expenses = [17.5, 20, 6, 18.5, 12.75, 3, 35.25]

suma = 0

for expense in expenses:
    suma = suma + expense

print ("You spent $", suma, sep="")


total = sum(expenses)

print ("Your spent a total of " + str(total) + " dollars.")