from ....exception import GameException

class InventoryException(GameException): pass


class ItemNotFound(InventoryException):
    """Raised when the item is not found in the inventory."""

class CapacityExceeded(InventoryException):
    """Raised when the inventory capacity is exceeded."""

class InvalidList(InventoryException):
    """Raised when the item is not in the list of valid items."""