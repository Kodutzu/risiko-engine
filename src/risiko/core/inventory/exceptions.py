from ..game.exception import GameException

class InventoryException(GameException): pass


class ItemNotFound(InventoryException):
    """Raised when the item is not found in the inventory."""

class CapcityExceeded(InventoryException):
    """Raised when the inventory capacity is exceeded."""