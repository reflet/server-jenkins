#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

"""
   シナリオ No.02 Python公式サイトで検索する
   
    ex)
    $ RUN_ENV='testing' && python /root/opt/ext02_python_org_search.py
"""
driver = webdriver.Remote(
    command_executor='http://selenium-hub:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME)

driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.quit()
