from typing import override

from .interface import MapperInterface
from ..core.effect.interface import EffectInterface
from ..core.effect.snapshot import EffectSnapshot

class EffectMapper(MapperInterface):

    @staticmethod
    @override
    def disassemble(
        interface: EffectInterface,
        snapshot: EffectSnapshot = EffectSnapshot
        ) -> EffectSnapshot:
        
        return snapshot(
            entity = interface.entity, 
            remaining_turns = interface.turns
            )