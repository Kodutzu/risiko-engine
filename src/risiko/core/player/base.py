from attrs import define, field, evolve
from attrs.validators import ge
from typing import Final, final

from .exception import PlayerDeadException

@define(frozen=True)
class PlayerBase:

    """
    Represents a player in the game with an ID and a number of charges (lives).
    
    """
    id: Final[str] 
    charges: int = field(validator=ge(0))

    @final
    def _lose_charges(self, amt: int) -> "PlayerBase":

        """
        Reduces the player's charges by the specified amount.

        Args:
            amt (int): The amount of charges to lose. Must be non-negative.

        Returns:
            PlayerBase: A new PlayerBase instance with updated charges.

        Raises:
            PlayerDeadException: If the player already has 0 charges.
            ValueError: If the amount to lose is negative.
        """

        if self.charges <= 0:
             raise PlayerDeadException(id=self.id, info="Player is already at 0 charges")
        
        if amt < 0:
            raise ValueError("Amount to lose must be non-negative.")
        
        new_charge_value = max(0, self.charges - amt)
        return evolve(self, charges=new_charge_value)
    
    @final
    def _gain_charges(self, amt: int) -> "PlayerBase":

        """
        Increases the player's charges by the specified amount.

        Args:
            amt (int): The amount of charges to add. Must be non-negative.

        Returns:
            PlayerBase: A new PlayerBase instance with updated charges.

        Raises:
            ValueError: If the amount to add is negative.
        """

        if amt < 0:
            raise ValueError("Amount to add must be non-negative.")
        
        new_charge_value = self.charges + amt
        return evolve(self, charges=new_charge_value)

