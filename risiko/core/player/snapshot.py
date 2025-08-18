from pydantic import BaseModel, Field
from typing import List, Tuple

class PlayerSnapshot(BaseModel):
    id: int = Field(default=0)
    charge: int = Field(default=4)
    inventory: List[str] = Field(default_factory=list)
    effects: List[Tuple[str,int]] = Field(default_factory=list)
