class UseCaseException(Exception):
    def __init__(self, message: Exception):
        self.message = message
        
class ScraperException(UseCaseException):
    pass

class UnknownException(UseCaseException):
    pass
        
@staticmethod
def create_from_exception(exception: Exception) -> 'UseCaseException':
    if(isinstance(exception, ScraperException)):
        return ScraperException(exception)
    else:
        return UnknownException(exception)


if(__name__ == '__main__'):
    try:
        raise ScraperException('This is a test')
    except UseCaseException as e:
        print(create_from_exception(e))