# Task 5 : Finance Calculator - Capstone Project by Alexandra Woodard
# The Finance Calculator allows the user to see either a calculation for simple or compound interest on an investment 
# or what they would owe each month to repay a home loan (bond). 
# Ask the user to input the word investment or bond; include an error message if the input is incorrect (use a while loop).
# The user inputs a number of details (for an investment - deposit, interest rate, term & simple or compound interest; for a bond - house value, interest rate & repayment months)
# and the program returns an interest due amount or a loan repayment amount.

import math

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
print(" ")
print(" ")

user_calc_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower().strip()

print(" ")

while True: 
    if user_calc_choice == "investment":
        print("You have selected " + user_calc_choice)
        break 
    elif user_calc_choice == "bond":
        print("You have selected " + user_calc_choice)
        break 
    else:
        print("You have not entered a valid response for this calculator. Please enter investment or bond.")
        print("  ")
        user_calc_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower().strip()
        print("  ")

if user_calc_choice == "investment":
    deposit = int(input("How much money are you depositing? "))
    interest_rate = int(input("What is your interest rate excluding the % (e.g. input 4 for 4%)? ")) 
    term = int(input("How many years do you plan to invest? ")) 
    interest = input("Do you want simple or compound interest? ").lower()
    if interest == "simple":
        print("Simple interest due on your investment is: ", end='')
        print((deposit * (1 + (((interest_rate)/100))*term))-deposit) 
    else :
        print("Compound interest due on your investment is: ", end='')
        print((deposit * ((1 + interest_rate/100)**term))-deposit) 

# For the example deposit amount of $100, a term of 20 years and an interest rate of 8%, simple interest due is $160 and compound interest due is $366

if user_calc_choice == "bond":
    house_value = int(input("Input the present value of your house "))
    bond_rate = int(input("What is your annual interest rate as a number excluding the % (e.g. input 4 for 4%)? "))
    monthly_int_rate = ((bond_rate)/100)/12                
    repayment_months = int(input("Over how many months will your loan be repaid? "))
    print("Your monthly repayment amount is : ", end='')
    print((monthly_int_rate*house_value)/(1-((1+monthly_int_rate)**-repayment_months)))

# For the example amount of $100,000, 120 months and an interest rate of 7%, the repayment amount is $1,161