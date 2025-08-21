from ._base_config import _BaseConfig as BaseConfig
from pydantic import Field
from typing import Tuple, Union
from ..constants.usable_entity import UsableEntity
from ..constants.shell import Shell

class ItemConfig(BaseConfig):
    entity: UsableEntity

class EffectConfig(BaseConfig):
    entity: UsableEntity
    remaining_turns: int

class InventoryConfig(BaseConfig):
    starting_items: Tuple[ItemConfig] = Field(default_factory=tuple)
    capacity: int = 4

class EffectorConfig(BaseConfig):
    effects: Tuple[EffectConfig] = Field(default_factory=tuple)

class PlayerConfig(BaseConfig):
    id: int
    initial_charges: int
    inventory_config: InventoryConfig = Field(default_factory=InventoryConfig)
    effector_config: EffectorConfig = Field(default_factory=EffectorConfig)

#========================================================================================

class MagazineConfig(BaseConfig):
    lives: int = Field(default=4,ge=1)
    blanks: int = Field(default=4,ge=1)
    tube: Tuple[Shell] = Field(default_factory=tuple)


class ShotgunConfig(BaseConfig):

    magazine: MagazineConfig = Field(default_factory=MagazineConfig)
    shell: Union[Shell, None] = Field(default=None)
    effector: EffectorConfig = Field(default_factory=EffectorConfig)
    live_dmg: int  = Field(default=1)

#Using Frozen to ensure that the config is immutable
class SessionConfig(BaseConfig):
    players: Tuple[PlayerConfig] 
    shotgun: ShotgunConfig 