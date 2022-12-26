import time

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#driver = webdriver.Chrome(executable_path=r'C:\Users\Mogilat Igor\Desktop\WebDriver\chromedriver.exe')
#driver.get('https://google.com')

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#САМЫЙ РАБОТАЮЩИЙ ТЕСТ ИЗ ВСЕХ
def test_driver_manager_chrome():
    service = ChromeService(executable_path=ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service)
    driver.get('https://google.com')

    time.sleep(2)

    search_input = driver.find_element("name", "q")

    search_input.clear()
    search_input.send_keys('first test')

    time.sleep(2)

    search_button = driver.find_element('name', 'btnK').click()

    time.sleep(2)

    driver.save_screenshot('result.png')


    driver.quit()

def test_driver_manager_chrome():
    service = ChromeService(executable_path=ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service)
    driver.get('https://google.com')

    time.sleep(2)

    search_input = driver.find_element("name", "q")

    search_input.clear()
    search_input.send_keys('first test')

    time.sleep(2)

    search_button = driver.find_element('name', 'btnK').submit()

    time.sleep(2)

    driver.save_screenshot('result.png')


    driver.quit()
