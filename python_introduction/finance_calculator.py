#Prompt the user for their monthly income
monthlyIncome = input("Enter your monthly income")

#Ask for their total monthly expenses
monthlyExpenses = input("Enter your total monthly expenses")

#Calculate the monthly savings
monthlySavings = int(monthlyIncome) - int(monthlyExpenses)

#Calculate the projected savings after one year
projectedSavings = monthlySavings * 12 + (monthlySavings * 12 * 0.05)

#Display the user’s monthly savings.
print (f"your monthly savings are ${monthlySavings}")

#Display the projected annual savings after including interest.
print(f"projected savings after one year, with interest, is: ${projectedSavings}")
