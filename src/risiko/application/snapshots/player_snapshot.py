from pydantic import BaseModel, Field
from .effector_snapshot import EffectorSnapshot
from .inventory_snapshot import InventorySnapshot

class PlayerSnapshot(BaseModel):
    id: str 
    charge: int = Field(default=4)
    effector: EffectorSnapshot = Field(default_factory=EffectorSnapshot)
