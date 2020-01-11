from selenium.webdriver import Chrome
import csv
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os

principal_amount = input("enter the principal amount: ")

down_payment = input("enter the down payment: ")

chrome_options = Options()

chrome_options.add_argument("--headless")

driver = Chrome("C:/Users/ASUS/Desktop/chromedriver.exe", options=chrome_options)

url = "https://www.bankofamerica.com/mortgage/mortgage-rates/"

driver.get(url)
time.sleep(3)

text_areas_one = driver.find_element_by_id('purchase-price-input-medium')

text_areas_one.clear()

text_areas_one.send_keys(principal_amount)

text_areas_two = driver.find_element_by_id('down-payment-input-medium')

text_areas_two.clear()

text_areas_two.send_keys(down_payment)

button_update = driver.find_element_by_id('update-button-medium')

button_update.click()

rates = driver.find_elements_by_class_name("update-partial")

thirty_y = rates[1].text

driver.close()

with open('rates.csv', "w", newline='') as rates:
	writer = csv.writer(rates)
	writer.writerow(["30 year rate"])
	writer.writerow([thirty_y])