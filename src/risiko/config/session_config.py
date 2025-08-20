from pydantic import BaseModel, Field
from typing import List, Union
from ..constants.usable_entity import UsableEntity
from ..constants.bullet import Bullet

class ItemConfig(BaseModel):
    entity: UsableEntity

class EffectConfig(BaseModel):
    entity: UsableEntity
    remaining_turns: int

class InventoryConfig(BaseModel):
    starting_items: List[ItemConfig] = Field(default_factory=list)
    capacity: int = 4

class EffectorConfig(BaseModel):
    effects: List[EffectConfig] = Field(default_factory=list)

class PlayerConfig(BaseModel):
    id: int
    initial_charges: int
    inventory_config: InventoryConfig = Field(default_factory=InventoryConfig)
    effector_config: EffectorConfig = Field(default_factory=EffectorConfig)

#========================================================================================

class MagazineConfig(BaseModel):
    lives: int = Field(default=4,ge=1, frozen=True)
    blanks: int = Field(default=4,ge=1, frozen=True)
    tube: List[Bullet] = Field(default_factory=list)

class ShotgunConfig(BaseModel):

    magazine: MagazineConfig = Field(default_factory=MagazineConfig)
    shell: Union[Bullet, None] = Field(default=None)
    effector: EffectorConfig = Field(default_factory=EffectorConfig)
    live_dmg: int  = Field(default=1)

class SessionConfig(BaseModel):
    players: List[PlayerConfig]
    shotgun: ShotgunConfig