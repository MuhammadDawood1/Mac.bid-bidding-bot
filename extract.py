from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import datetime
from time import sleep

def driverFunc():
     #option = webdriver.ChromeOptions()

    chromeOptions = webdriver.ChromeOptions()
        
    #chromeOptions.add_argument('--headless')
    chromeOptions.add_argument('--disable-notifications')

    #chromeOptions.add_argument("window-size=1280,800")

    chromeOptions.add_argument('--disable-extensions')

    chromeOptions.add_argument("--user-data-dir="+os.getcwd()+"\\src\\UserData")

    chromeOptions.add_argument("--disable-plugins-discovery")
    chromeOptions.add_argument("--start-maximized")
    chromeOptions.add_argument('--ignore-certificate-errors')
    chromeOptions.add_argument('--ignore-ssl-errors')

    # For older ChromeDriver under version 79.0.3945.16
    chromeOptions.add_experimental_option("excludeSwitches", ["enable-automation"])
    chromeOptions.add_experimental_option('useAutomationExtension', False)
    # For ChromeDriver version 79.0.3945.16 or over
    chromeOptions.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(options=chromeOptions)
    driver.implicitly_wait(5)
    return driver


def extractItems(driver):
    
    driver.get('https://www.mac.bid/account/watchlist')
    sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    sleep(6)
    items = driver.find_elements(by=By.XPATH, value='//*[@class="card product-card d-block d-sm-flex flex-row"]')

    listOfItems = []
    for item in items:
        itemDict = {}
        days = int(item.find_element(by=By.CLASS_NAME, value='cz-countdown-days').text.split('d')[0])
        hours = int(item.find_element(by=By.CLASS_NAME, value='cz-countdown-hours').text.split('h')[0])
        miniutes = int(item.find_element(by=By.CLASS_NAME, value='cz-countdown-minutes').text.split('m')[0])
        #print(days,hours,miniutes)
        timeInSeconds = (days*24*60 + hours*60 + miniutes)*60 
        itemDict['timeRemaining'] = timeInSeconds
        #dropDown = item.find_element_by_tag_name('select')
        #options = dropDown.find_elements_by_tag_name('option')
        itemDict['lotNumber'] = item.find_element(by=By.TAG_NAME, value='a').get_attribute('href')
        #itemDict['lotNumber'] = item.find_element(by=By.XPATH, value='//*[@class="product-meta d-block font-size-xs pb-1"]/a').get_attribute('href')
        itemDict['currentBid'] = float(item.find_element(by=By.XPATH, value='//*[@class="h1 font-weight-normal text-accent mb-0 mr-4"]/span').text.replace('$',''))
        itemDict['bidNowBtn'] = item.find_element(by=By.XPATH, value='//*[@class="btn btn-primary btn-shadow btn-block"]')
        listOfItems.append(itemDict)

    #print(listOfItems)
    return(listOfItems)



# d = driverFunc()
# d.get('https://www.mac.bid')
# sleep(3600)
#print(extractItems(driverFunc()))
#print(listOfItems)
# cardInWatchList = 'card product-card d-block d-sm-flex flex-row'
# addProtectionBtn = 'btn btn-success mx-1 my-2 btn-block' #btn btn-success mx-1 my-2 btn-block
# takeTheRiskBtn = 'btn btn-danger mx-1 my-2 btn-block' #btn btn-danger mx-1 my-2 btn-block


# outbidclass = 'alert alert-warning mb-2'
# winningClass = 'alert alert-dark font-size-sm mb-2 py-1'
# retailAndBidPrices = 'h1 font-weight-normal text-accent mb-0 mr-4'
# registertoBidBtnClass = 'btn btn-block btn-primary'
# registerToBidBtnText = 'Register to Bid'


# ModalClass = 'modal-content' #register to bid form class/see screen shot