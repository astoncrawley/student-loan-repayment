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