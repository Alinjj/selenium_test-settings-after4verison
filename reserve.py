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



def test_driver_manager_chrome():
    service = ChromeService(executable_path=ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service)
    driver.get("https://petfriends.skillfactory.ru/")
    time.sleep(2)

    search_btn = driver.find_element(By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]").click()
    time.sleep(2)

    have_acc_btn = driver.find_element(By.LINK_TEXT,u"У меня уже есть аккаунт" ).click()
    time.sleep(2)

    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys(login)

    pass_input = driver.find_element(By.ID, "pass")
    pass_input.send_keys(password)
    enter_btn = driver.find_element(By.XPATH,'/html/body/div/div/form/div[3]/button').submit()
    assert driver.find_element(By.TAG_NAME,'h1').text == 'PetFriends'
    time.sleep(2)
    my_pets = driver.find_element(By.LINK_TEXT,u'Мои питомцы').click()
    time.sleep(2)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//th[@scope='row']/img")))
    have_all_pets = driver.find_elements(By.XPATH,"//th[@scope='row']/img")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='.col-sm-4 left']")))
    stat = driver.find_element(By.XPATH,"//div[@class='.col-sm-4 left']").text.split('\n')
    number = stat[1].split(' ')
    number = int(number[1])
    assert number == len(have_all_pets)






    driver.close()
    driver.quit()