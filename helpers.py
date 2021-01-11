import requests
import urllib
import re
import json
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


### Naake clean this up


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
    

    


class Scraper(object):
    def __init__(self, endpoint):
        self.driver = Driver().driver
        self.endpoint = endpoint
        self.current_url = ''
        self.pull()
        

    def pull(self):
        try:
            self.driver.get(self.endpoint)
        except:
            return False
        time.sleep(4)
        self.current_url = self.driver.current_url
        return True

    def scrape(self,scroll_time):
        """
        Scrapes and returns bs4 tree for the page in the supplied url
        Gets past age verification and has a scroll param
        """
        self.scroll(scroll_time)
        time.sleep(5)
        html = self.driver.execute_script("return document.documentElement.innerHTML")
        siteData = SOUP(html, 'html.parser')
        return siteData

    def scroll(self, scroll_time):
        for i in range(1,scroll_time):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)


    def delete(self):
        """
        Destructor to make sure the driver is closed
        """
        self.driver.close()       


class League(Scraper):
    def __init__(self, endpoint):
        super().__init__(endpoint)
        # These are tokens for auth

    def getData(self):
        siteinfo = self.scrape(5)
        return siteinfo
        