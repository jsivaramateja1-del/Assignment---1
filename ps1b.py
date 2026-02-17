'''
ps1b.py
Assignment 1 - Part B : Saving with a Raise
Name      : JOGIPARTHI VENKATA AUDI SIVA RAMA TEJA
PRN       : 250200278
APP NO    : CDS/2025/1401
'''

'''
This program calculates the number of months required to save enough
for the down payment of a house when the salary increases every 6 months.
'''

# Input Values
while True:
    try:
        annual_salary = float(input("Enter your starting annual salary: "))
        if annual_salary <= 0:
            print("Salary must be positive.")
            continue
        break
    except ValueError:
        print("Invalid input.")

while True:
    try:
        portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
        if portion_saved < 0 or portion_saved > 1:
            print("Saving rate must be between 0 and 1.")
            continue
        break
    except ValueError:
        print("Invalid input.")

while True:
    try:
        total_cost = float(input("Enter the cost of your dream home: "))
        if total_cost <= 0:
            print("Cost must be positive.")
            continue
        break
    except ValueError:
        print("Invalid input.")

while True:
    try:
        semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
        if semi_annual_raise < 0:
            print("Raise cannot be negative.")
            continue
        break
    except ValueError:
        print("Invalid input.")


#  Initial Calculations and given data

down_payment = total_cost * 0.25
current_savings = 0.0

monthly_salary = annual_salary / 12

annual_return_rate = 0.04
monthly_return_rate = annual_return_rate / 12

months = 0


# loop until savings reac down payment

while current_savings < down_payment:

    # Add interest earned on savings
    current_savings += current_savings * monthly_return_rate

    # Add saving from salary
    current_savings += monthly_salary * portion_saved

    # month completed Counts
    months += 1

    # salary raise every 6 months
    if months % 6 == 0:
        annual_salary = annual_salary * (1 + semi_annual_raise)
        monthly_salary = annual_salary / 12


#  OUTPUT 
print("Number of months:", months)
