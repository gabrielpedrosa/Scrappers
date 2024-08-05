from ..base.base_scrapper import BaseScraper
from selenium.webdriver.common.by import By

class ExampleScraper(BaseScraper):
    def get_data(self):
        self.open_page("https://www.example.com")
        element = self.find_element(By.ID, "element_id")
        return element.text