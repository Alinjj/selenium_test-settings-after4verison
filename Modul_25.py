from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_all_pets_check(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//th[@scope='row']/img")))
    have_all_pets = driver.find_elements(By.XPATH, "//th[@scope='row']/img")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='.col-sm-4 left']")))
    stat = driver.find_element(By.XPATH, "//div[@class='.col-sm-4 left']").text.split('\n')
    number = stat[1].split(' ')
    number = int(number[1])
    assert number == len(have_all_pets)
    driver.close()
    driver.quit()



def test_50procent_have_photo(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//th[@scope='row']/img")))
    images = driver.find_elements(By.XPATH, "//th[@scope='row']/img")
    counter = 0
    for i in range(len(images)):
        if images[i].get_attribute("src") != '':
            counter +=1
    stat = driver.find_element(By.XPATH, "//div[@class='.col-sm-4 left']").text.split('\n')
    number = stat[1].split(' ')
    number = int(number[1])
    assert counter >= number // 2
    driver.close()
    driver.quit()


def test_name_age_type(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='all_my_pets']/table/tbody/tr[1]/td[1]")))
    name = driver.find_elements(By.XPATH,'//*[@id="all_my_pets"]/table/tbody/tr[1]/td[1]')

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='all_my_pets']/table/tbody/tr[1]/td[2]")))
    animal_type = driver.find_elements(By.XPATH,'//*[@id="all_my_pets"]/table/tbody/tr[1]/td[2]')

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='all_my_pets']/table/tbody/tr[1]/td[3]")))
    age = driver.find_elements(By.XPATH,'//*[@id="all_my_pets"]/table/tbody/tr[1]/td[3]')
    array_desc = [age,name,animal_type]
    for i in range(len(array_desc)):
        assert array_desc[i] != ''

def test_same_names(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//td[@class='smart_cell']/preceding-sibling::td[3]" )))
    names = driver.find_elements(By.XPATH, "//td[@class='smart_cell']/preceding-sibling::td[3]")
    names_list = []
    for i in range(len(names)):
        names_list.append(names[i].text)

        assert len(set(names_list)) == len(names_list)

def test_unique_pets(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//td[@class='smart_cell']/preceding-sibling::td[3]")))
    name = driver.find_elements(By.XPATH,'//td[@class="smart_cell"]/preceding-sibling::td[3]')

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//td[@class='smart_cell']/preceding-sibling::td[2]")))
    animal_type = driver.find_elements(By.XPATH,'//td[@class="smart_cell"]/preceding-sibling::td[2]')

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//td[@class='smart_cell']/preceding-sibling::td[1]")))
    age = driver.find_elements(By.XPATH,'//td[@class="smart_cell"]/preceding-sibling::td[1]')

    array_desc = []
    array_desc2 = []
    array_desc3 = []
    total_pet = []

    for i in range(len(name)):
        array_desc.append(name[i].text)

    for i in range(len(age)):
        array_desc2.append(age[i].text)

    for i in range(len(animal_type)):
        array_desc3.append(animal_type[i].text)

    for(x,y,z) in zip(array_desc,array_desc3,array_desc3):
        total_pet.append(x+y+z)
        assert len(set(total_pet)) == len(total_pet)




























