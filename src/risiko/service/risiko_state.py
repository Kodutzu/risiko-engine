from __future__ import annotations
from attrs import define, field
from typing import Type
import random

from .managers import PlayerManager, TurnManager
from ..core import ShotgunInterface,ShotgunBase


@define(frozen=True)
class RisikoState:
    """
    Represents the live snapshot of the game state.
    This class is an immutable data container.
    State modifications should be performed via Processors.
    """

    shotgun: ShotgunInterface = field(factory=ShotgunBase)
    player: PlayerManager = field(factory=PlayerManager)
    turns: TurnManager = field(factory=TurnManager)
