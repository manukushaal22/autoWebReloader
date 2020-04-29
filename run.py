from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Constants:
    OPERATING_SYSTEM = "win"  # possible values - "mac" , "win , "lin"
    CHROME_VERSION = "81"  #possible values - "80" , "81" , "83"
    CUSTOM_WEBDRIVER_PATH = None

    WEBSITE_URL = "https://accenturelearning.tekstac.com/course/view.php?id=21"
    USERNAME = "madhuri21121998@gmail.com"
    PASSWORD = "Madhuri2112"
    RELOAD_INTERVAL_SECONDS = 60 * 5

    USERNAME_ELEMENT_NAME = "username"
    PASSWORD_ELEMENT_NAME = "password"
    LOGINBUTTON_ELEMENT_ID = "loginbtn"

def generateEnvironmentSpecificURL(constants):
    if constants.CUSTOM_WEBDRIVER_PATH is not None:
        return constants.CUSTOM_WEBDRIVER_PATH
    url =  "resources/v"+constants.CHROME_VERSION+"/"+constants.OPERATING_SYSTEM+"/chromedriver"
    if constants.OPERATING_SYSTEM == "win":
        url += '.exe'
    return url

def log(data):
    return "["+str(datetime.now())+"]" + " INFO "+data

if __name__=="__main__":
    constants = Constants()

    driver = webdriver.Chrome(generateEnvironmentSpecificURL(constants))
    print(log("Driver Loaded"))
    driver.get(constants.WEBSITE_URL)
    print(log("Redirected to url: " + constants.WEBSITE_URL))
    time.sleep(2)
    driver.find_element_by_name(constants.USERNAME_ELEMENT_NAME).send_keys(constants.USERNAME)
    print(log("Username Entered: " + constants.USERNAME))
    time.sleep(2)
    driver.find_element_by_name(constants.PASSWORD_ELEMENT_NAME).send_keys(constants.PASSWORD)
    print(log("Password Entered."))
    time.sleep(2)
    driver.find_element_by_id(constants.LOGINBUTTON_ELEMENT_ID).send_keys(Keys.ENTER)
    print(log("Logged In."))
    time.sleep(2)
    reload_count = 0
    while True:
        time.sleep(constants.RELOAD_INTERVAL_SECONDS)
        driver.refresh()
        reload_count+=1
        print(log("Reloaded page for "+str(reload_count)+" time(s) now with interval: "+str(constants.RELOAD_INTERVAL_SECONDS)+" seconds."))

