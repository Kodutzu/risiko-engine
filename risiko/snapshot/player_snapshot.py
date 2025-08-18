from pydantic import BaseModel, Field
from typing import List, Dict

class PlayerSnapshot(BaseModel):
    id: int = Field(default=0)
    charge: int = Field(default=4)
    inventory: List[str] = Field(default_factory=list)
    effects: Dict[str,int] = Field(default_factory=dict)
