from pydantic import BaseModel, Field
from ..effect.snapshot import EffectorSnapshot
from ..inventory.snapshot import InventorySnapshot

class PlayerSnapshot(BaseModel):
    id: str = Field(default=0)
    charge: int = Field(default=4)
    inventory: InventorySnapshot = Field(default_factory=InventorySnapshot)
    effector: EffectorSnapshot = Field(default_factory=EffectorSnapshot)
