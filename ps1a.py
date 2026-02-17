'''
ps1a.py
Assignment 1 - Part A : House Hunting
Name      : JOGIPARTHI VENKATA AUDI SIVA RAMA TEJA
PRN       : 250200278
APP NO    : CDS/2025/1401
'''
'''
Collaborators:
    1) S. Siva Harsha
    2) B. Chandra Shekar Reddy
'''

'''
This program calculates how many months are required to save enough money
for the down payment of a house.

We assume:
Down payment = 25% of the total cost of the house
Savings grow at 4% annual return (investment interest)

The program works month-by-month and keeps adding:
1) Interest on current savings
2) A portion of the monthly salary
'''


# ---------------------- INPUT SECTION ----------------------

# Getting the annual salary
while True:
    try:
        annual_salary = float(input("Enter your annual salary: "))
        if annual_salary <= 0:
            print("Please enter a positive salary.")
            continue
        break
    except ValueError:
        print("Invalid input. Enter a numeric value.")

# Getting the saving rate (as decimal)
while True:
    try:
        portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
        if portion_saved < 0 or portion_saved > 1:
            print("Saving rate must be between 0 and 1.")
            continue
        break
    except ValueError:
        print("Invalid input. Enter a numeric value.")

# Getting house cost
while True:
    try:
        total_cost = float(input("Enter the cost of your dream home: "))
        if total_cost <= 0:
            print("Cost must be positive.")
            continue
        break
    except ValueError:
        print("Invalid input. Enter a numeric value.")


# ---- INITIAL CALCULATIONS ----

# 25% of the house price is down payment
down_payment = total_cost * 0.25

# 0 savings at the beginning
current_savings = 0.0

# Convert annual salary to monthly salary
monthly_salary = annual_salary / 12

# Convert annual interest rate to monthly
annual_return_rate = 0.04
monthly_return_rate = annual_return_rate / 12

# Counter to track number of months passed
months = 0


# Loop until savings surpass down payment

while current_savings < down_payment:

    # bank adds interest to the existing savings
    current_savings += current_savings * monthly_return_rate

    # we add the saved portion of this month's salary
    current_savings += monthly_salary * portion_saved

    # One month completed
    months += 1


# ---------------------- OUTPUT ----------------------
print("Number of months:", months)
