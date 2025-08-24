from typing import override

from .interface import MapperInterface
from ..core.effector.interface import EffectorInterface
from ..core.effector.snapshot import EffectorSnapshot
from .effect_mapper import EffectMapper

class EffectorMapper(MapperInterface):
    
    @staticmethod
    @override
    def disassemble(

        interface: EffectorInterface,
        snapshot: EffectorSnapshot = EffectorSnapshot
        
          ) -> EffectorSnapshot:
        
        return snapshot(
            effect_list= [EffectMapper.disassemble(effect) for effect in interface.effector]
            )