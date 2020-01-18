from get_banks import *

"""functions inputs"""
principal_amount = input("enter the principal amount: ")  
down_payment = input("enter the down payment: ")
city = 'Los Angeles'
county = 'Los Angeles'
two_l_state = 'CA'
credit_score = 'Very Good'
state = 'california'
zip_code = ""  # to be defined

======================================================================================================

"""calling functions"""
functions_list = [get_ally_bank(), get_citi(down_payment, principal_amount, city, county, two_l_state),
                  get_us_bank(), get_hsbc(down_payment, principal_amount),
                  get_wells_fargo(), get_bank_of_america(principal_amount, down_payment),
                  get_nbkc(down_payment, principal_amount, state, credit_score),
                  get_schwab(down_payment, principal_amount, zip_code, credit_score)]



for function in functions_list:  # iterate through every func w/o breaking code
    try:
        function
    except:
        pass






