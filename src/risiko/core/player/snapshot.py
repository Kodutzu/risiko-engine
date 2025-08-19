from pydantic import BaseModel, Field
from typing import List, Tuple
from ..effect.snapshot import EffectorSnapshot
from ..inventory.snapshot import inventorySnapshot

class PlayerSnapshot(BaseModel):
    id: int = Field(default=0)
    charge: int = Field(default=4)
    inventory: inventorySnapshot = Field(default_factory=inventorySnapshot)
    effector: EffectorSnapshot = Field(default_factory=EffectorSnapshot)
