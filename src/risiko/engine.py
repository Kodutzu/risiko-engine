from .handlers.game_handler import GameHandler
from .config.engine_config import EngineConfig
from pydantic import BaseModel, Field, PrivateAttr


class RisikioEngine(BaseModel):

    _game_handler = GameHandler = PrivateAttr(default_factory=GameHandler)
    config = EngineConfig = Field(default_factory=EngineConfig)

    # More Development to be done!
    # Engine Role - To Manage Multiple Sessions
    #allow Custom Handler through Engineconfig
