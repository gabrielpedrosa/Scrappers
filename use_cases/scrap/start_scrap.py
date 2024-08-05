from domain.repositories.scraper_repository import ScraperRepository
from domain.models.scraper_model import ScraperModel
from ..use_case import UseCase, Configuration, Request, Response
from rx import Observable

class StartScrap(UseCase):
    def __init__(self, configuration: Configuration, scraper_repository: ScraperRepository) -> None:
        super().__init__(configuration)
        self.scraper_repository = scraper_repository
        
    class Request(Request):
        def __init__(self, url: str) -> None:
            self.url = url
            
    class Response(Response):
        def __init__(self, data: ScraperModel) -> None:
            self.data = data
        
    def process(self, request: Request) -> Observable:
        return self.scraper_repository.start_scrap(request.url)