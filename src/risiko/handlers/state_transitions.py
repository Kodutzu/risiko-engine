from ..constants.game_state import GameState
from typing import Dict, List
from dataclasses import dataclass, field

@dataclass
class StateMachine:

    state: GameState = field(default=GameState.INITIALIZE)
    transitions: Dict[GameState, List[GameState]] = field(default_factory=dict)

    def __post_init__(self):
            
            self.transitions = {
                GameState.INITIALIZE: [GameState.ROUND_START],
                GameState.ROUND_START: [GameState.ITEM_DISTRIBUTION, GameState.PLAYER_TURN],
                GameState.ITEM_DISTRIBUTION: [GameState.PLAYER_TURN],
                GameState.PLAYER_TURN: [GameState.AWAITING_ACTION, GameState.ROUND_END],
                GameState.AWAITING_ACTION: [GameState.ITEM_USE, GameState.SHOOT],
                GameState.ITEM_USE: [GameState.AWAITING_ACTION],
                GameState.SHOOT: [GameState.RESOLVE_ACTION],
                GameState.RESOLVE_ACTION: [GameState.EFFECT_TICK],
                GameState.EFFECT_TICK: [GameState.TURN_TRANSITION],
                GameState.TURN_TRANSITION: [GameState.PLAYER_TURN],
                GameState.ROUND_END: [GameState.RESULT],
                GameState.RESULT: [GameState.GAMEOVER],
                GameState.GAMEOVER: [GameState.INITIALIZE]

            }
        
    #Take these method in GameHandler

    # def _can_transition(self, to_state:GameState) -> bool:
 
    #     return (self.state != to_state) and (to_state in self.transitions.get(self.state, []))
    
    # def transition(self, to_state:GameState) -> None:
    #     if self._can_transition(to_state):
    #         self.state = to_state
    #     else:
    #         raise Exception(f"Invalid state transition: {self.state} -> {to_state}")