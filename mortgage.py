from selenium.webdriver import Chrome
import csv
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
from sys import platform

principal_amount = input("enter the principal amount: ")  

down_payment = input("enter the down payment: ")

chrome_options = Options()

chrome_options.add_argument("--headless")  # option to not open browser when scraping 

def extension():
	if platform == "linux" or platform == "linux2":
		return ""  #linux2
	elif platform == "darwin":
		return ""  # OS X
	elif platform == "win32":
		return ".exe"  # Windows...


driver_path = os.path.join(os.getcwd(), ('chromedriver' + extension()))  # get directory in which python script and webdriver are and get the right format for chrome webdriver

driver = Chrome(driver_path, options=chrome_options)

url = "https://www.bankofamerica.com/mortgage/mortgage-rates/"

driver.get(url)
time.sleep(3)

text_areas_one = driver.find_element_by_id('purchase-price-input-medium')  # find text are of mortgage principal amount

text_areas_one.clear()  # clear it

text_areas_one.send_keys(principal_amount)  # enter principal amount you entered at the beginning

text_areas_two = driver.find_element_by_id('down-payment-input-medium')  # find text are of down payment 

text_areas_two.clear()

text_areas_two.send_keys(down_payment)  # enter down payment 

button_update = driver.find_element_by_id('update-button-medium')

button_update.click()

rates = driver.find_elements_by_class_name("update-partial")  # find all text that changes with the update button

thirty_y = rates[1].text  # get the 2nd text as its the 30y 

driver.close()

with open('rates.csv', mode="w") as rates:
	writer = csv.writer(rates)
	writer.writerow(["30 year rate"])
	writer.writerow([thirty_y])
#algum