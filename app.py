#!/usr/bin/python

import time
import traceback
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('C:\\Users\\nsadmin\\Desktop\\chromedriver')

"""
Reddit Login Information
"""
username = '<USERNAME>'
password = '<PASSWORD>'
driver.get("https://old.reddit.com/")
elem = driver.find_element_by_name("user")
elem.send_keys(username)
elem = driver.find_element_by_name("passwd")
elem.send_keys(password)
elem.send_keys("\n")
time.sleep(5)
time.sleep(10)

with open('reddit.txt','r') as f:
    for line in f:
        try:
            driver.get(line.rstrip())
            elem  = driver.find_element_by_link_text('subscribe')
            elem.click()
            time.sleep(5)
        except Exception as e:
            print '{}'.format(line.rstrip())
            print e
driver.delete_all_cookies()
driver.close()
