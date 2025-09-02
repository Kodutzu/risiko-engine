

class ItemException(Exception):
    """Base exception for item-related errors."""


class InvalidItem(ItemException):
    """Raised when the item is invalid."""

class InventoryException(Exception): 
    """Base exception for inventory-related errors."""


class ItemNotFound(InventoryException):
    """Raised when the item is not found in the inventory."""

class CapacityExceeded(InventoryException):
    """Raised when the inventory capacity is exceeded."""

class InvalidList(InventoryException):
    """Raised when the item is not in the list of valid items."""