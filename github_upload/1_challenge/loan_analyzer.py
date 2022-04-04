#coding: utf-8
import csv
from pathlib import Path


""" Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""


loan_costs = [500, 600, 200, 1000, 450]


# How many loans are in the list?
# @TODO: Use the `len` function to calculate the total number of loans in the list.
# Print the number of loans from the list

number_of_loans = len(loan_costs)
print(f"There are {number_of_loans} loans oustanding.")


# What is the total of all loans?
# @TODO: Use the `sum` function to calculate the total of all loans in the list.
# Print the total value of the loans

total_of_all_loans = sum(loan_costs)
print(f"Total sum of all loans: {total_of_all_loans}")



# What is the average loan amount from the list?
# @TODO: Using the sum of all loans and the total number of loans, calculate the average loan price.
# Print the average loan amount

average_loan_price = total_of_all_loans / number_of_loans
print(f"The average loan amount is: ${average_loan_price}")


"""Part 2: Analyze Loan Data.
 
Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable.

    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
"""


# Given the following loan data, you will need to calculate the present value for the loan

loan_price = 500
remaining_months = 9
repayment_interval = 12
future_value = 1000
annual_discount_rate = .02


# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
future_value = loan_price * ((1 + (annual_discount_rate * repayment_interval)) ** remaining_months)

print(f"The future value of the loan is: ${future_value: .2f}")
print(f"{remaining_months} months remaining on the loan")

# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months

present_value = future_value / (1 + (annual_discount_rate / repayment_interval)) ** remaining_months
print(f"Fair value of loan is: ${present_value: .2f}")



# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

if present_value <= loan_price:
    print("This loan has potential! INVEST NOW!")
elif present_value > loan_price:
    print("This loan is too expensive at the moment! DO NOT RISK!")



"""Part 3: Perform Financial Calculations.
Perform financial calculations using functions.
1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""


# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 9,
    "repayment_interval": "monthly",
    "future_value": 1000,
}

# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.

def present_value(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1 + (annual_discount_rate / 12)) ** remaining_months


# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.

    print(f"The present value of the loan is ${present_value}")
    return present_value



"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than or equal to 500
    b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# @TODO: Create an empty list called `inexpensive_loans`

inexpensive_loans = [loan_price, remaining_months, repayment_interval, future_value]


# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list

def filter_inexpensive_loans(loans, loan_price):

    for inexpensive_loans in loans:
        if loan_price <= (loans[future_value, 500]):
            inexpensive_loans.append(loans)
    return filter_inexpensive_loans


# @TODO: Print the `inexpensive_loans` list
print(f"These loans are inexpensive: {inexpensive_loans}")


"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""


# Set the output header

header = f"Loan price: {loan_price}, Remaining months: {remaining_months: .2f}, Repayment interval: {repayment_interval}, Future value: ${future_value: .2f}"
print(header)


# Set the output file path

output_path = Path("inexpensive_loans.csv")

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
def load_csv(csvpath):
   
    with open(csvpath, "w") as csvfile:

        data = [",",",",","]

        csvwriter = csv.writer(csvfile, delimiter="")

        csvwriter.writeheader
        
        # Read the CSV data
        for row in csv.writer:
            data.append(loan_price,inexpensive_loans)
        return data