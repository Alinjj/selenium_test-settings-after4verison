import time
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By





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
    email_input.send_keys('test_qa_python@mail.ru')

    pass_input = driver.find_element(By.ID, "pass")
    pass_input.send_keys('RL3uPTo4icy)')

    enter_btn = driver.find_element(By.XPATH,'/html/body/div/div/form/div[3]/button').submit()
    assert driver.find_element(By.TAG_NAME,'h1').text == 'PetFriends'
    time.sleep(2)

    my_pets = driver.find_element(By.LINK_TEXT,u'Мои питомцы').click()
    time.sleep(2)
    #str_pets = driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(":")[1]








########################################################
# тест для проверки, что все карточки питомцев не пустые
########################################################
    # images = driver.find_elements(By.CSS_SELECTOR,'.card-deck .card-img-top')
    # names = driver.find_elements(By.CSS_SELECTOR,'.card-deck .card-title')
    # descriptions = driver.find_elements(By.CSS_SELECTOR,'.card-deck .card-text')
    # for i in range(len(names)):
    #     assert images[i].get_attribute('src') != None
    #     assert names[i].text != None
    #     assert descriptions[i].text != None
########################################################


    # if find_h1 == 'PetFriend':
    #     driver.save_screenshot('Screen_h1')
    # else:
    #     raise Exception('Not_find_h1')
    # if driver.current_url == 'https://petfriends.skillfactory.ru/all_pets':
    #     driver.save_screenshot('total_pf.png')
    # else:
    #     raise Exception('Login Error')



    driver.quit()



#@pytest.fixture(autouse=True)
