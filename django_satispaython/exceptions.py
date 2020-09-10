class DjangoSatispaythonException(Exception):
    def __init__(self, message):
        super().__init__(message)


class ResponseStatusError(DjangoSatispaythonException):
    def __init__(self, response, message=None):
        self.response = response
        super().__init__(message)