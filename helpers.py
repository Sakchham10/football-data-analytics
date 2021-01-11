import time
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup as SOUP
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

chrome_options = Options()
chrome_options.add_argument("--headless")


class Driver(object):
    driver = None
    drivermanager = ChromeDriverManager().install()

    def __init__(self):
        self.new_instance()

    def new_instance(self):
        self.driver = webdriver.Chrome(self.drivermanager, options=chrome_options)
    
    def get(self, endpoint):
        self.driver.get(endpoint)
        return self.driver

    def close(self):
        self.driver.close()

def scrape(endpoint, scroll=5):
    driver = Driver().driver
    current_url = ''
    try:
        driver.get(endpoint)
    except:
        return False
    time.sleep(2)
    current_url = driver.current_url
    for i in range(1,scroll):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
    time.sleep(5)
    html = driver.execute_script("return document.documentElement.innerHTML")
    siteData = SOUP(html, 'html.parser')
    return siteData