## Loan Qualifier App

This program will create an loan application that will ease the way for the average consumer to execute applyiomng for a loan. The app will calculate a users credit score, debt-to-income ratio, value of the loan(s), and maximum loan amount. Goal of this program is the give access to everyone from their phone and access banking products. 

---


## ATM app

Scripted with Python3 on Visual Studio Code with a dev environment with dependencies of:

for stable versions use 

* fire==0.3.1
* questionary==1.5.2  

"""Determine which loans the user qualifies for.

    Loan qualification criteria is based on:
        - Credit Score
        - Loan Size
        - Debit to Income ratio (calculated)
        - Loan to Value ratio (calculated)

    Args:
        bank_data (list): A list of bank data.
        credit_score (int): The applicant's current credit score.
        debt (float): The applicant's total monthly debt payments.
        income (float): The applicant's total monthly income.
        loan (float): The total loan amount applied for.
        home_value (float): The estimated home value.

    Returns:
        A list of the banks willing to underwrite the loan.

ATM App uses MODULAR programming therefore all functions run independently and bugs can be fixed easily.



---

## Installation Guide

Make sure the csv is running and all the dependencies are in order. Built on VS code. 

---


## Usage

Returns:
        Returns the applicant's financial information.
    """

    credit_score = questionary.text("What's your credit score?").ask()
    debt = questionary.text("What's your current amount of monthly debt?").ask()
    income = questionary.text("What's your total monthly income?").ask()
    loan_amount = questionary.text("What's your desired loan amount?").ask()
    home_value = questionary.text("What's your home value?").ask()


    #
    credit_score = int(credit_score)
    debt = float(debt)
    income = float(income)
    loan_amount = float(loan_amount)
    home_value = float(home_value)

    return (credit_score, debt, income, loan_amount, home_value)

These is the data that will be retrieved to enable lending on the Loan application.
---

## Contributors

Rensley Ramos
Linked-in: Rensley Ramos
Twitter: rensley_ramos



---



                                Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/


