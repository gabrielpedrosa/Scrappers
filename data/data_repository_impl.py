from webscraper.domain.repositories.data_repository import DataRepository
from webscraper.domain.models.data_model import DataModel
from webscraper.config.webdriver_config import WebDriverConfig
from selenium.webdriver.common.by import By

class DataRepositoryImpl(DataRepository):
    def get_data(self) -> DataModel:
        driver = WebDriverConfig.get_driver()
        driver.get("https://www.example.com")
        element = driver.find_element(By.ID, "element_id")
        data = element.text
        driver.quit()
        return DataModel(data)