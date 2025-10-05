import numpy as np
import math



def calculate_daily_interest_rate(interest_rate, days_in_year=365):
    """function that calculates the daily interest rate

    Args:
        interest_rate (float): interest rate
        days_in_year (int, optional): number of days in a year. Defaults to 365.

    Returns:
        float: daily interest rate
    """
    return (1 + interest_rate)**(1/days_in_year) - 1



def annual2monthly_interest(annual_interest):
    return (1 + annual_interest)**(1/12) - 1



def calculate_min_repayment(gross_salary, annual_thresh=28470.00, charge=0.09):
    """function that calculates the minimum monthly repayment of the student loan

    Args:
        gross_salary (float): gross annual salary
        annual_thresh (float): repayment threshold
        charge (float): repayment percentage

    Returns:
        int: minimum monthly repayment amount
    """
    
    monthly_thresh = annual_thresh/12
    
    monthly_repayment = ((gross_salary/12)-monthly_thresh)*charge
    
    if monthly_repayment < 0:
        monthly_repayment = 0
            
    return math.floor(monthly_repayment)



def calculate_interest(rpi, income, low_thresh=28470.00, high_thresh=51245.00):
    """function that calculates the student loan interest rate based on the retail price index and income

    Args:
        rpi (float): retail price index
        income (float): annual income

    Returns:
        float: interest rate to be applied
    """
    
    if income < low_thresh: 
        interest_rate = rpi
    elif income > high_thresh:
        interest_rate = rpi + 3
    else:
        interest_rate = rpi + 3 * ((income - low_thresh) / (high_thresh - low_thresh))
    
    return interest_rate







def calculatePlan2Repayments(salary, annual_thresh):
    monthly_thresh = annual_thresh/12
    charge = 0.09
    
    monthly_repayment = ((salary/12)-monthly_thresh)*charge
    
    if monthly_repayment < 0:
        monthly_repayment = 0
        
    return monthly_repayment


def calculatePostgradRepayments(salary):
    month_thresh = 1750
    charge = 0.06
    
    monthly_repayment = ((salary/12)-month_thresh)*charge
    
    if monthly_repayment < 0:
        monthly_repayment = 0
        
    return monthly_repayment


min_repayment = calculatePlan2Repayments(gross_salary, repayment_thresh)



# def calculateAnnualPlan2Repayments(loan_remaining, min_repayment, interest_rate, extra_payment):
#     new_loan_remaining = (loan_remaining-(min_repayment*12)-(extra_payment*12))
#     if new_loan_remaining <= 0:
#         return 0
#     else:
#         return new_loan_remaining


def calculateAnnualPlan2Repayments(loan_remaining, min_repayment, interest_rate, extra_repayment):
    total_minimum_repayments = 0
    total_extra_repayments = 0

    for month in range(12):
        loan_remaining -= min_repayment
        if loan_remaining <= 0:
            total_minimum_repayments += abs(loan_remaining)
            return 0, total_minimum_repayments, total_extra_repayments
        else:
            total_minimum_repayments += min_repayment
    
        loan_remaining -= extra_repayment
        if loan_remaining <= 0:
            total_extra_repayments += abs(loan_remaining)
            return 0, total_minimum_repayments, total_extra_repayments
        else:
            total_extra_repayments += extra_repayment
    
    return loan_remaining, total_minimum_repayments, total_extra_repayments



val = loan_remaining
val_an = []

for i in range(30):
    val = (val-(min_repayment*12))*study_interest
    val_an.append(val)
    
plt.plot(val_an)
plt.show()

print("Total amount paid over 30 years")
print(min_repayment*12*30)





def calculateInterest(initial_pot, monthly_addition, interest_rate, years):
    
    annual_pot = [0]
    
    for i in range(years):
        end_pot = initial_pot + (monthly_addition*12)
        annual_average = initial_pot + (end_pot - initial_pot)
        initial_pot = annual_average * interest_rate
        annual_pot.append(initial_pot)
    
    return annual_pot