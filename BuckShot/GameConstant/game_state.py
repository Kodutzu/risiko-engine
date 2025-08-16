from enum import Enum, auto

class GameState(Enum):
    # Game Setup Phase
    INITIALIZE = auto()
    ROUND_START = auto()         
    ITEM_DISTRIBUTION = auto() 
    
    # Player Turn Phase
    PLAYER_TURN = auto()         
    AWAITING_ACTION = auto() 
    ACTION_VALIDATION = auto() 
    
    # Action Execution Phase  
    ITEM_USE = auto()           
    SHOOT = auto()              
    RESOLVE_ACTION = auto() 
    
    # Turn Management Phase
    EFFECT_TICK = auto() 
    TURN_TRANSITION = auto() 
    
    # Game End Phase
    ROUND_END = auto()          
    RESULT = auto()             
    GAMEOVER = auto() 

