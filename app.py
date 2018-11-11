#!/usr/bin/python
'''Reddit mass subscriber'''

import time
from sys import argv
from selenium import webdriver

# Check if proper params are passed
if len(argv) != 5:
    print("Command:python app.py <path to chromedriver> <username> <password> <path to reddit.txt>")
else:
    PATH_DRIVER = argv[1]
    USER_NAME = argv[2]
    PASSWORD = argv[3]
    PATH_FILE = argv[4]
    DRIVER = webdriver.Chrome(PATH_DRIVER)

    """
    Reddit Login Information
    """
    DRIVER.get("https://old.reddit.com/")
    ELEM = DRIVER.find_element_by_name("user")
    ELEM.send_keys(USER_NAME)
    ELEM = DRIVER.find_element_by_name("passwd")
    ELEM.send_keys(PASSWORD)
    ELEM.send_keys("\n")
    time.sleep(5)
    time.sleep(10)

    with open(PATH_FILE, 'r') as f:
        for line in f:
            try:
                DRIVER.get(line.rstrip())
                ELEM = DRIVER.find_element_by_link_text('subscribe')
                ELEM.click()
                time.sleep(5)
            except Exception as err:
                print('{}'.format(line.rstrip()))
                print(err)
    DRIVER.delete_all_cookies()
    DRIVER.close()
