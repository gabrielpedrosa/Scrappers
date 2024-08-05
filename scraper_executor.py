from .config.webdriver_config import WebDriverConfig
from .use_cases.use_case import Configuration
from concurrent.futures import ThreadPoolExecutor

class ScraperExecutor:
    def __init__(self, scraperRepository) -> None:
        self.driver = WebDriverConfig().get_driver()
        self.configuration = Configuration(ThreadPoolExecutor())
        self.scraperRepository = scraperRepository
        self.use_cases = []
    
    def add_use_case(self, use_case):
        self.use_cases.append(use_case)
        
    def execute(self):
        for use_case in self.use_cases:
            use_case.execute()
            
    def execute_use_case(self, use_case):
        use_case.execute()