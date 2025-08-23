from ..constants.game_state import GameState
from typing import Dict, List
from dataclasses import dataclass, field
from ..config.state_transitions import STATE_TRANSITIONS

@dataclass
class StateMachine:

    state: GameState = field(default=GameState.INITIALIZE)
    transitions: Dict[GameState, List[GameState]] = field(default_factory=lambda: STATE_TRANSITIONS)

    #Take these method in GameHandler

    # def _can_transition(self, to_state:GameState) -> bool:
 
    #     return (self.state != to_state) and (to_state in self.transitions.get(self.state, []))
    
    # def transition(self, to_state:GameState) -> None:
    #     if self._can_transition(to_state):
    #         self.state = to_state
    #     else:
    #         raise Exception(f"Invalid state transition: {self.state} -> {to_state}")