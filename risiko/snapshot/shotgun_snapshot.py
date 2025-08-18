from pydantic import BaseModel, Field
from typing import List, Dict, Union

class ShotgunSnapshot(BaseModel):
    magazine: List[str] = Field(default_factory=list)
    shell: Union[str, None ] = Field(default=None)
    live_dmg: int  = Field(default=1)
    effects: Dict[str, int] = Field(default_factory=dict)
