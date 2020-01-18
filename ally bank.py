from selenium.webdriver import Chrome
import csv
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from constants import DRIVER_PATH
from selenium.webdriver.support.ui import Select


city = 'Los Angeles'
county = 'Los Angeles'
state = 'CA'


with open(path, mode="a") as rates:
        writer = csv.writer(rates)
        writer.writerow(['Thirty year rate', 'Bank'])


def get_ally_bank(path):
    """scrape ally bank and get their 30y mortgage rate"""
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # option to not open browser when scraping 
    driver = Chrome(DRIVER_PATH, options=chrome_options)
    url = 'https://www.ally.com/home-loans/mortgage/'
    driver.get(url)
    time.sleep(3)
    thirty_y = driver.find_element_by_xpath('//*[@id="rates"]/div[2]/div/figure/table/tbody/tr[1]/td[4]')  # find 30 y rate 
    thirty_y.text
    driver.close()
    with open(path, mode="a") as rates:
        writer = csv.writer(rates)
        writer.writerow([thirty_y, 'Ally Bank'])
    print("ally bank complete")


def get_citi(down_payment, principal_amount, path, city, county, state):
    """scrape citi and get their 30y mort rate"""
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # option to not open browser when scraping 
    driver = Chrome(DRIVER_PATH, options=chrome_options)
    url = 'https://online.citi.com/US/nccmi/purchase/ratequote/flow.action?fromLanding=true&selectedOption=CUSTOM&selectedOptionValue=CUSTOMpurChaseLanding&JFP_TOKEN=H49AIYPN'
    driver.get(url)
    time.sleep(3)
    property_use = Select(driver.find_element_by_xpath('//*[@id="propertyUse"]'))
    property_use.select_by_visible_text('I will live in this home')  # used to select a drop down menu value
    cnty = Select(driver.find_element_by_xpath('//*[@id="propCounty"]'))  # select county
    cnty.select_by_visible_text(county)
    cty = driver.find_element_by_xpath('//*[@id="propCity"]')  # select city
    cty.clear()
    cty.send_keys(city)
    stte = Select(driver.find_element_by_xpath('//*[@id="propState"]'))  # select state
    stte.select_by_visible_text(state)
    purchase_price = driver.find_element_by_xpath('//*[@id="purchPrice"]')
    purchase_price.clear()
    purchase_price.send_keys(principal_amount)
    loan_amount = driver.find_element_by_xpath('//*[@id="desiredLoanAmount"]')
    loan_amount.clear()
    loan_amount.send_keys(str(float(principal_amount) - float(down_payment)))  # convert string vars to floats to be able to substract then back to string
    credit_score = driver.find_element_by_xpath('//*[@id="creditScoreGoodLabel"]')
    credit_score.click()
    thirty_y = driver.find_element_by_xpath('//*[@id="FeaturedProducts-container"]/div[1]/div/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/p[2]')
    thirty_y.text
    driver.close()
    with open(path, mode="a") as rates:
        writer = csv.writer(rates)
        writer.writerow([thirty_y, 'Citi Bank'])
    print("citi bank complete")


def get_us_bank(path):
    """scrape us bank and get their 30y mortgage rate"""
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # option to not open browser when scraping 
    driver = Chrome(DRIVER_PATH, options=chrome_options)
    url = 'https://www.usbank.com/home-loans/mortgage/conventional-fixed-rate-mortgages.html'
    driver.get(url)
    time.sleep(3)
    thirty_y = driver.find_element_by_xpath('//*[@id="mortgagesRateTable"]/div/div/div/div[3]/table/tbody/tr[2]/td[2]')  # find 30y rate
    thirty_y.text
    driver.close()
    with open(path, mode="a") as rates:
        writer = csv.writer(rates)
        writer.writerow([thirty_y, 'US Bank'])
    print("us bank complete")