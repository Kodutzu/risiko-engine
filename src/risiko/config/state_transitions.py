from ..constants.game_state import GameState

STATE_TRANSITIONS = {
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