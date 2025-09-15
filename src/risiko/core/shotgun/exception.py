class ShotgunException(Exception):
    """Base exception for the shotgun component"""
    pass

class ShotgunNotLoadedException(ShotgunException):

    """Raised when an operation requires a loaded shotgun, but it is not."""

    def __init__(self, message="Shotgun is not loaded"):
        """
        Initializes the ShotgunNotLoadedException.

        Args:
            message (str, optional): The error message. Defaults to "Shotgun is not loaded".
        """
        self.message = message
        super().__init__(self.message)
