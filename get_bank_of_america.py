from selenium.webdriver import Chrome
import csv
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from constants import DRIVER_PATH


def get_bank_of_america(principal_amount, down_payment, path):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # option to not open browser when scraping 
    driver = Chrome(DRIVER_PATH, options=chrome_options)
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
    with open(path, mode="w") as rates:
        writer = csv.writer(rates)
        writer.writerow(["30 year rate"])
        writer.writerow([thirty_y])
    print("Bank of America complete")