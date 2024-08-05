class Result:
    class Success:
        def __init__(self, value) -> None:
            self.value = value
            pass
        
    class Failure:
        def __init__(self, error) -> None:
            self.error = error
            