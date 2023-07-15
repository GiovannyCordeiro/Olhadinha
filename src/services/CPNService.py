from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class CPNBroserService:
    def extract(store):

        driver = webdriver.Chrome()
        driver.get('')
        driver.implicitly_wait(10)

        inputElement = driver.find_element(By.CSS_SELECTOR, "#query")
        inputElement.send_keys(f"{store}")
        inputElement.send_keys(Keys.ENTER)

        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'rewardsTag-cashback'))
        )

        textElement = driver.find_elements(By.CSS_SELECTOR, ".rewardsTag-cashback")[1].text
        cashbackPercentage = textElement[7:8]
        return cashbackPercentage