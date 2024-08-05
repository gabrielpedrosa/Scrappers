from abc import ABC, abstractmethod
from concurrent.futures import Executor
from typing import Generic, TypeVar, Callable
from rx import Observable
from rx import operators as ops
from rx.scheduler import ThreadPoolScheduler

# from domain.repositories.scraper_repository import ScraperRepository
from domain.models.scraper_model import ScraperModel
from .result import Result
from .use_case_exception import create_from_exception

Req = TypeVar('Req', bound='Request')
Resp = TypeVar('Resp', bound='Response')

class UseCase(ABC, Generic[Req, Resp]):
    def __init__(self, configuration: 'Configuration'):
        self.configuration = configuration
    
    def execute(self, request: Req) -> Observable:
        return self.process(request).pipe(
            ops.map(lambda result: Result.Success(result)),
            ops.subscribe_on(ThreadPoolScheduler(self.configuration.executor)),
            ops.on_error_return(lambda e: Result.Error(create_from_exception(e)))
        )
        
    @abstractmethod
    def process(self, request: Req) -> Observable:
        pass

class Configuration:
    def __init__(self, executor: Executor):
        self.executor = executor
    
class Request(ABC):
    pass

class Response(ABC):
    pass