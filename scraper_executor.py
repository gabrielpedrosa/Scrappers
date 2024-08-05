from .use_cases.use_case import Configuration
from concurrent.futures import ThreadPoolExecutor
from .config.webdriver_config import WebDriverConfig
from typing import List, Dict, TypedDict
from .use_cases.use_case import UseCase, Request, Response


class UseCaseDict(TypedDict):
    use_case: UseCase
    request: Request
    response: Response

class ScraperExecutor:
    def __init__(self) -> None:
        self.driver = WebDriverConfig().get_driver()
        self.use_cases: List[UseCaseDict] = []
    
    def add_use_case(self, use_case, use_case_request = None):
        use_case_dict: UseCaseDict = {
            "use_case": use_case,
            "request": use_case_request,
            "result": None
        }
        self.use_cases.append(use_case_dict)
        
    def execute(self):
        for use_case_dict in self.use_cases:
            use_case = use_case_dict["use_case"]
            request = use_case_dict["request"]
            
            result = use_case.execute(request)
            
            use_case_dict["result"] = result
        
    def get_results(self) -> List[UseCaseDict]:
        return [use_case_dict["result"] for use_case_dict in self.use_cases]