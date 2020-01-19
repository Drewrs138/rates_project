import time
import selenium
from get_banks import *

"""functions arguments"""
principal_amount = input("enter the principal amount: ")  
down_payment = input("enter the down payment: ")
city = 'Los Angeles'
county = 'Los Angeles'
two_l_state = 'CA'
credit_score = 'Very Good'
state = 'california'
zip_code = ""  # to be defined

'================================'

"""calling functions"""
functions_list = [
    ("Ally Bank", get_ally_bank),
    ("Citi Bank", lambda : get_citi(down_payment, principal_amount, city, county, two_l_state)),
    ("US Bank", get_us_bank),
    ("HSBC", lambda : get_hsbc(down_payment, principal_amount)),
    ("Wells Fargo", get_wells_fargo),
    ("Bank of America", lambda : get_bank_of_america(principal_amount, down_payment)),
    ("NBKC", lambda : get_nbkc(down_payment, principal_amount, state, credit_score)),
    ("Schwab", lambda : get_schwab(down_payment, principal_amount, zip_code, credit_score))
]



for function in functions_list:  # iterate through every func w/o breaking code
    try:
        start = time.time()
        function[1]()
        end = time.time()
        print(f"{function[0]} completed execution in {end-start}s")
    except:
        end = time.time()
        print(f"{function[0]} failed execution in {end-start}s")
        