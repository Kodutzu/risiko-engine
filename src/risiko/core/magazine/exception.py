from ..exception import CoreException

class MagazineException(CoreException):
    """Base exception for magazine-related errors."""
    pass

class MagazineEmptyException(MagazineException):
    """Raised when an operation is attempted on an empty magazine."""
    pass
