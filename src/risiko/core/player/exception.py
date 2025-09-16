from ..exception import CoreException

class PlayerException(CoreException):
    """
    Base class for player exceptions.
    """
    ...

class PlayerDeadException(PlayerException):
    """
    Exception raised when an action is attempted on a player who is already dead (has 0 charges).
    """
    def __init__(self, id: str, info: str) -> None:
        """
        Initializes the PlayerDeadException.

        Args:
            id (str): The ID of the dead player.
            info (str): Additional information about the exception.
        """
        super().__init__(f"Player with ID '{id}' is dead - {info}")

class PlayerIDNotFoundException(PlayerException):
    """
    Exception raised when a player with a specified ID is not found.
    """
    def __init__(self, id, info: str) -> None:
        """
        Initializes the PlayerIDNotFoundException.

        Args:
            id (str): The ID of the player not found.
            info (str): Additional information about the exception.
        """
        super().__init__(f"Player with ID '{id}' not found, {info}")

class PlayerIDExistsException(PlayerException):
    """
    Exception raised when attempting to add a player with an ID that already exists.
    """
    def __init__(self, id, info) -> None:
        """
        Initializes the PlayerIDExistsException.

        Args:
            id (str): The ID of the player that already exists.
            info (str): Additional information about the exception.
        """
        super().__init__(f"Player with ID '{id}' already exists.")

class PlayerInvalidTurnException(PlayerException):
    """
    Exception raised when a player attempts an action out of their turn.
    """
    def __init__(self, id, info) -> None:
        """
        Initializes the PlayerInvalidTurnException.

        Args:
            id (str): The ID of the player who attempted an action out of turn.
            info (str): Additional information about the exception.
        """
        super().__init__(f"Player with ID '{id}' is not the current player.")