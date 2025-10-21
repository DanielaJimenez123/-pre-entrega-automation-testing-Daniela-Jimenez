import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
URL="https://www.saucedemo.com/"
NAME="standard_user"
CLAVE="secret_sauce"
def get_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    return driver
driver= get_driver()
def login_saucedemo(driver):
    driver.get(URL)
    driver.find_element(By.NAME,"user-name").send_keys(NAME)
    driver.find_element(By.NAME,"password").send_keys(CLAVE)
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )
    return True
    time.sleep(3)
if __name__ == "__main__":
    driver = get_driver()
    login_saucedemo(driver)
    driver.quit()
