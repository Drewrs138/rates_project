from selenium.webdriver import Chrome
import csv
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from constants import DRIVER_PATH
from selenium.webdriver.support.ui import Select


city = 'Los Angeles'
county = 'Los Angeles'
two_l_state = 'CA'
credit_score = 'Very Good'
state = 'california'


with open(path, mode="a") as rates:
        writer = csv.writer(rates)
        writer.writerow(['Thirty year rate', 'Bank'])


def get_driver(url):
    """driver for the desired bank"""
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # option to not open browser when scraping 
    driver = Chrome(DRIVER_PATH, options=chrome_options)
    driver.get(url)
    time.sleep(3)
    return driver


def get_ally_bank(path):
    """scrape ally bank and get their 30y mortgage rate"""
    get_driver('https://www.ally.com/home-loans/mortgage/')
    thirty_y = driver.find_element_by_xpath('//*[@id="rates"]/div[2]/div/figure/table/tbody/tr[1]/td[4]')  # find 30 y rate 
    thirty_y.text
    driver.close()
    with open(path, mode="a") as rates:
        writer = csv.writer(rates)
        writer.writerow([thirty_y, 'Ally Bank'])
    print("ally bank complete")


def get_citi(down_payment, principal_amount, path, city, county, two_l_state):
    """scrape citi and get their 30y mort rate"""
    get_driver('https://online.citi.com/US/nccmi/purchase/ratequote/flow.action?fromLanding=true&selectedOption=CUSTOM&selectedOptionValue=CUSTOMpurChaseLanding&JFP_TOKEN=H49AIYPN')
    property_use = Select(driver.find_element_by_xpath('//*[@id="propertyUse"]'))
    property_use.select_by_visible_text('I will live in this home')  # used to select a drop down menu value
    cnty = Select(driver.find_element_by_xpath('//*[@id="propCounty"]'))  # select county
    cnty.select_by_visible_text(county)
    cty = driver.find_element_by_xpath('//*[@id="propCity"]')  # select city
    cty.clear()
    cty.send_keys(city)
    stte = Select(driver.find_element_by_xpath('//*[@id="propState"]'))  # select state
    stte.select_by_visible_text(two_l_state)
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
    get_driver('https://www.usbank.com/home-loans/mortgage/conventional-fixed-rate-mortgages.html')
    thirty_y = driver.find_element_by_xpath('//*[@id="mortgagesRateTable"]/div/div/div/div[3]/table/tbody/tr[2]/td[2]')  # find 30y rate
    thirty_y.text
    driver.close()
    with open(path, mode="a") as rates:
        writer = csv.writer(rates)
        writer.writerow([thirty_y, 'US Bank'])
    print("us bank complete")

    
def get_hsbc(down_payment, principal_amount, path):
    """scrape hsbc bank and get their 30y mortgage rate"""
    get_driver('https://www.us.hsbc.com/home-loans/products/mortgage-rates/#preapproved')
    loan_amount = float(principal_amount) - float(down_payment) 
    if 200000 < loan_amount < 400000:
        thirty_y = driver.find_element_by_xpath('//*[@id="content_main_tile_1"]/div[2]/p')
        thirty_y.text
        thirty_y.split('|')  
        thirty_y = thirty_y[1]  # get the correct rate as the string displays two interest rates
        thirty_y.strip('% APR')
    elif loan_amount > 400000:
        thirty_y = driver.find_element_by_xpath('//*[@id="content_main_tile_7"]/div[2]/p/span')
        thirty_y.text
        thirty_y.strip("% APR") 
    driver.close()
    with open(path, mode="a") as rates:
        writer = csv.writer(rates)
        writer.writerow([thirty_y, 'HSBC Bank'])
    print("hsbc bank complete")


def get_schwab(down_payment, principal_amount, path, zip_code, credit_score):
    """scrape schwab bank and get their 30y mortgage rate"""
    get_driver('https://www.schwab.com/public/schwab/banking_lending/mortgage_rate_calculator')
    loan_purpose = driver.Select(find_element_by_xpath('//*[@id="calc_LoanPurpose"]'))
    loan_purpose.select_by_visible_text('Purchase')
    purchase_price = driver.find_element_by_xpath('//*[@id="calc_PurchasePrice"]')
    purchase_price.send_keys(principal_amount)
    down_pay = driver.find_element_by_xpath('//*[@id="calc_DownPayment"]')
    down_pay.send_keys(down_payment)
    zip_c = driver.find_element_by_xpath('//*[@id="calc_Zip"]')
    zip_c.send_keys(zip_code)
    property_use = Select(driver.find_element_by_xpath('//*[@id="calc_OccupancyType"]'))
    property_use.select_by_visible_text('Primary')
    property_type = Select(driver.find_element_by_xpath('//*[@id="calc_PropertyType"]'))
    property_type.select_by_visible_text('Single Family')
    crdt_score = Select(driver.find_element_by_xpath('//*[@id="calc_CreditScore"]'))
    crdt_score.select_by_visible_text(credit_score)  
    get_results = driver.find_element_by_xpath('//*[@id="calc_Submit"]')
    get_results.click()  # the previous code fills the form to get the interest rate
    time.sleep(11)
    thirty_y = driver.find_element_by_xpath('//*[@id="tab_fixed"]/div[2]/div[2]/div[2]/div[2]/div[3]/span[2]')
    thirty_y.text
    driver.close()
    with open(path, mode="a") as rates:
        writer = csv.writer(rates)
        writer.writerow([thirty_y, 'charles schwab'])
    print("charles schwab bank complete")


def get_nbkc(down_payment, principal_amount, path, state, credit_score):
    """scrape nbkc bank and get their 30y mortgage rate"""
    get_driver('https://www.schwab.com/public/schwab/banking_lending/mortgage_rate_calculator')
    loan_kind = driver.find_element_by_xpath('//*[@id="check-rates-form"]/div[1]/div[2]/label[1]')
    loan_kind.click()
    home_value = driver.find_element_by_xpath('//*[@id="home-value"]')
    home_value.send_keys(principal_amount)
    down_pay = driver.find_element_by_xpath('//*[@id="down-payment"]')
    down_pay.send_keys(down_payment)
    state = Select(driver.find_element_by_xpath('//*[@id="loan-state"]'))
    state.select_by_visible_text(state)
    credit_score = Select(driver.find_element_by_xpath('//*[@id="credit-rating"]'))
    credit_score.select_by_visible_text(credit_score)
    see_rates = driver.find_element_by_xpath('//*[@id="check-rates-form"]/div[5]/button')
    see_rates.click()
    thirty_y = driver.find_element_by_xpath('//*[@id="30-year-fixed"]/div/div[2]/div[7]/div[2]/span')
    thirty_y.text
    driver.close()
    with open(path, mode="a") as rates:
    writer = csv.writer(rates)
    writer.writerow([thirty_y, 'nbkc'])
    print("nbkc bank complete")