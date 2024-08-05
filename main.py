from use_cases.scrap.start_scrap import StartScrap
from use_cases.scrap.get_data_use_case import GetDataUseCase
from use_cases.use_case import Configuration
from scrapers.scraper_repository_impl import ScraperRepositoryImpl
from config.webdriver_config import WebDriverConfig
from concurrent.futures import ThreadPoolExecutor

def main():
    driver = WebDriverConfig().get_driver()
    
    configuration = Configuration(ThreadPoolExecutor())
    scraperRepository = ScraperRepositoryImpl(driver)
    useCase = GetDataUseCase(configuration, scraperRepository)
    startScrap = StartScrap(configuration, scraperRepository)
    
    startScrap.execute(StartScrap.Request("https://br.investing.com/crypto"))
    # useCase.execute(GetDataUseCase.Request("https://br.investing.com/crypto"))

if __name__ == "__main__":
    main()