from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class BaseScraper:
    def __init__(self, driver) -> None:
        self.driver = driver
        
    def open_page(self, url):
        self.driver.get(url)
    
    def maximize_window(self):
        self.driver.maximize_window()

    def find_element(self, by, value):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, value)))

    def find_elements(self, by, value):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((by, value)))
    
    def implicitly_wait(self, seconds: int):
        self.driver.implicitly_wait(seconds)
        
    def wait(self, seconds: int):
        sleep(seconds)

    def close(self):
        self.driver.quit()