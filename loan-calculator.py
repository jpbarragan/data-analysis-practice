# Get details of loan

money_owed = float(input("How much money do you owe, in dollars?\n"))
interest_rate = float(input("What is the annual percentage rate of the loan?\n"))
payment = float(input("How much do you pay each month?\n"))
months = int(input("How many months do you want to see the results for?\n"))

monthly_rate = interest_rate/100/12

for i in range(months):
    # Calculate interest to pay
    interest_paid = money_owed*monthly_rate

    # Added interest
    money_owed = money_owed + interest_paid

    if (money_owed - payment < 0):
        print ("The last payment is", money_owed)
        print ("You finished paying the loan in", i+1, "months")
        break

    # Make payment
    money_owed = money_owed - payment

    print ("Paid ", payment, "of which", interest_paid, "was interest")
    print ("Now I owe", money_owed)