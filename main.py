from get_bank_of_america import get_bank_of_america


principal_amount = input("enter the principal amount: ")  
down_payment = input("enter the down payment: ")
get_bank_of_america(principal_amount, down_payment, "rates.csv")
get_wells_fargo(principal_amount, down_payment, "rates.csv")