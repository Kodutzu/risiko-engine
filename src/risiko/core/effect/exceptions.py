class EffectException(Exception):
    """Base exception for all effect-related exceptions."""


class InvalidEffect(EffectException):
    """Raised when an effect is invalid."""


class EffectNotFound(EffectException):
    """Raised when an effect is not found."""


class DuplicateEffect(EffectException):
    """Raised when an effect is already applied."""
