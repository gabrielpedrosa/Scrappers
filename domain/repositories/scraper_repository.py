from abc import ABC, abstractmethod
from rx import Observable
from base.base_scrapper import BaseScraper

class ScraperRepository(ABC, BaseScraper):
    @abstractmethod
    def start_scrap(self, url: str) -> Observable:
        pass
    
    @abstractmethod
    def authenticate(self, username: str, password: str) -> Observable:
        pass
    
    
    @abstractmethod
    def get_data(self, url: str) -> Observable:
        pass