

class ApplicationError(Exception):
    """
    error class to represent application level errors
    """
    def __init__(self, code, message):
        """
        ApplicationError class constructor
        :param code: represents error code
        :param message: represents error message
        """
        self.error_code = code
        self.error_message = message
        super().__init__(code, message)
