from .exceptions import InvalidEffect
from ..effect.base import EffectBase

class EffectorValidator:
    
    @staticmethod #Moving it to effector/validator.py
    def validate_items(effect: EffectBase) -> EffectBase:

        if not isinstance(effect, EffectBase):
                raise InvalidEffect(f"Invalid Effect: {type(effect)}")
        return effect