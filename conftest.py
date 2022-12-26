import time
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Data import login, password

# @pytest.fixture(autouse=True)
# def driver():
#     service = ChromeService(executable_path=ChromeDriverManager().install())
#
#     driver = webdriver.Chrome(service=service)
#     driver.get("https://petfriends.skillfactory.ru/")
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//button[@onclick=\"document.location='/new_user';\"]"))).click()
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, u"У меня уже есть аккаунт"))).click()
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"email"))).send_keys(login)
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "pass"))).send_keys(password)
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/form/div[3]/button'))).submit()
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, u'Мои питомцы'))).click()
#
#     yield driver
#     driver.close()
#     driver.quit()

@pytest.fixture(autouse=True)
def driver():
   service = ChromeService(executable_path=ChromeDriverManager().install())
   driver = webdriver.Chrome(service=service)
   driver.implicitly_wait(10)
   driver.get('http://petfriends.skillfactory.ru/login')
   WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'email'))).send_keys(login)
   WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'pass'))).send_keys(password)
   WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]'))).click()
   WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Мои питомцы'))).click()

   yield driver
   driver.quit()



