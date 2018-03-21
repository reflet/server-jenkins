#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

"""
   シナリオ No.01 Qiitaページを閲覧する
   
    ex)
    $ RUN_ENV='testing' && python /root/opt/ext01_qiita_view.py
"""
driver = webdriver.Remote(
    command_executor='http://selenium-hub:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME)

driver.get("http://qiita.com/reflet")
driver.quit()
