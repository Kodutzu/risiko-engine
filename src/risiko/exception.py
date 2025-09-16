"""
Risiko Library Exceptions
"""

from .core.exception import CoreException
from .core.magazine.exception import (
    MagazineException,
    MagazineEmptyException,
)
from .core.player.exception import (
    PlayerException,
    PlayerDeadException,
    PlayerIDNotFoundException,
    PlayerIDExistsException,
    PlayerInvalidTurnException,
)
from .core.shotgun.exception import (
    ShotgunException,
    ShotgunLoadedException,
    ShotgunUnLoadedException
)

from .core.shell.exception import ShellException, ShellNotFoundException
__all__ = [
    "CoreException",
    "MagazineException",
    "MagazineEmptyException",
    "PlayerException",
    "PlayerDeadException",
    "PlayerIDNotFoundException",
    "PlayerIDExistsException",
    "PlayerInvalidTurnException",
    "ShotgunException",
    "ShotgunLoadedException",
    "ShotgunUnLoadedException",
    "ShellException",
    "ShellNotFoundException"
    
]
