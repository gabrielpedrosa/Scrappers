from domain.repositories.scraper_repository import ScraperRepository
from domain.models.scraper_model import ScraperModel
from config.webdriver_config import WebDriverConfig
from selenium.webdriver.common.by import By
from rx import Observable

class ScraperRepositoryImpl(ScraperRepository):
    def start_scrap(self, url: str) -> Observable:
        self.open_page(url)
        self.implicitly_wait(20)
        self.maximize_window()
        self.wait(600)
    
    def authenticate(self, username: str, password: str) -> Observable:
        pass
    
    def get_data(self, url: str) -> Observable:
        element = self.find_element(By.ID, "element_id")
        data = element.text
        self.close()
        return ScraperModel(data)