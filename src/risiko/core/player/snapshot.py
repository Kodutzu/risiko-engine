from pydantic import BaseModel, Field
from ..effector.snapshot import EffectorSnapshot
from ..inventory.snapshot import InventorySnapshot

class PlayerSnapshot(BaseModel):
    id: str 
    charge: int = Field(default=4)
    inventory: InventorySnapshot = Field(default_factory=InventorySnapshot)
    effector: EffectorSnapshot = Field(default_factory=EffectorSnapshot)
