class InvalidLicensePlate(Exception):
    """Exception raised for invalid license plate.

    Attributes:
        message -- explanation of the error
    """
    def __init__(self, message="Invalid license plate was given"):
        self.message = message
        super().__init__(self.message)

class UnexpectedSiteContent(Exception):
    """Exception raised when the dmr site has been changed and dmr.py doesn't support the change.

    Attributes:
        message -- explanation of the error
    """
    def __init__(self, message="DMR content has been updated, and the used version of dmr.py doesn't support the change."):
        self.message = message
        super().__init__(self.message)

class MissingToken(Exception):
    """Exception raised when the dmr site haven't given a token where it was expected to be.

    Attributes:
        message -- explanation of the error
    """
    def __init__(self, message="DMR token was not found, this may be a temporary error or could be a change in the way the DMR site handles requests that the current version of dmr.py doesn't support."):
        self.message = message
        super().__init__(self.message)