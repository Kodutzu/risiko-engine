from ..exception import CoreException


class ShellException(CoreException):
    """
    Base exception for the shell component
    """

    ...


class ShellNotFoundException(ShellException):
    """
    Exception raised when a shell with a specified ID is not found.
    """

    ...


class InvalidShell(ShellException):
    """
    Exception raised when a shell passed is incorrect
    """
