from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/Users/User/selenium_test/selenium_test/chromedriver")
driver.get('https://google.com')
driver.find_element(By.XPATH) 