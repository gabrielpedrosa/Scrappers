from use_cases.scrap.start_scrap import StartScrap
from use_cases.scrap.get_data_use_case import GetDataUseCase
from use_cases.use_case import Configuration
from scrapers.scraper_repository_impl import ScraperRepositoryImpl
from config.webdriver_config import WebDriverConfig
from concurrent.futures import ThreadPoolExecutor
from .scraper_executor import ScraperExecutor

def main():
    scrap_executor = ScraperExecutor()
    
    configuration = Configuration(ThreadPoolExecutor())
    scraperRepository = ScraperRepositoryImpl(scrap_executor.driver)
    
    # getData = GetDataUseCase(configuration, scraperRepository)
    scrap_executor.add_use_case(
        use_case=StartScrap(configuration, scraperRepository),
        use_case_request=StartScrap.Request("https://br.investing.com/crypto")
    )
    
    scrap_executor.execute()
    
    
    # startScrap.execute(StartScrap.Request("https://br.investing.com/crypto"))
    # useCase.execute(GetDataUseCase.Request("https://br.investing.com/crypto"))

if __name__ == "__main__":
    main()