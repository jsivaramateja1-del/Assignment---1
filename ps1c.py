'''
ps1c.py
Assignment 1 - Part C : Finding the Right Amount to Save
Name      : JOGIPARTHI VENKATA AUDI SIVA RAMA TEJA
PRN       : 250200278
APP NO    : CDS/2025/1401'''

"""
We now need to find WHAT percentage of salary must be saved
in order to afford the down payment within 36 months.

We do NOT try every possible value.

Instead, we use Bisection Search:
We repeatedly guess the middle saving rate and check whether
the savings are too low or too high.
"""

# ---------------------- CONSTANT VALUES ----------------------

total_cost = 1000000
down_payment = total_cost * 0.25
months = 36

semi_annual_raise = 0.07
monthly_return_value = 0.04 / 12

# ---------------------- INPUT ----------------------
annual_salary = float(input("Enter the starting salary: "))


# ---------------------- IMPOSSIBLE CASE CHECK ----------------------
# Try saving 100% salary

current_savings = 0.0
monthly_salary = annual_salary / 12

for month in range(1, months + 1):

    current_savings += current_savings * monthly_return_value
    current_savings += monthly_salary

    if month % 6 == 0:
        monthly_salary *= (1 + semi_annual_raise)

if current_savings < down_payment - 100:
    print("It is not possible to pay the down payment in three years.")

else:

    # ---------------------- BISECTION SEARCH ----------------------

    low = 0
    high = 10000
    steps = 0

    while True:
        steps += 1

        mid = (low + high) // 2
        portion_saved = mid / 10000

        current_savings = 0.0
        monthly_salary = annual_salary / 12

        # simulate 36 months
        for month in range(1, months + 1):

            current_savings += current_savings * monthly_return_value
            current_savings += monthly_salary * portion_saved

            if month % 6 == 0:
                monthly_salary *= (1 + semi_annual_raise)

        # check closeness
        if abs(current_savings - down_payment) <= 100:
            break
        elif current_savings < down_payment:
            low = mid
        else:
            high = mid

    print("Best savings rate: %.4f"%(portion_saved)) 
    print("Steps in bisection search:", steps)
