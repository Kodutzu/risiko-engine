from ..exception import CoreException

class MagazineException(CoreException):
    """
    Base exception for the magazine component

    """
    ...

class MagazineEmptyException(MagazineException):
    """
    Exception raised when the magazine is empty

    """

    def __init__(self, msg: str = "Magazine is empty") -> None:
        super().__init__(msg)

    ...