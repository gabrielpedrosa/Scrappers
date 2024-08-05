from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class WebDriverConfig:
    @staticmethod
    def get_driver() -> webdriver: 
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")  # Executar em modo headless
        driver = webdriver.Chrome(service=service, options=options)
        return driver