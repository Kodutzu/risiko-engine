from pydantic import BaseModel, Field
from typing import Dict, Any
class EngineConfig(BaseModel):
    """Configuration for the entire engine, including dependencies."""
    custom_handlers: Dict[str, Any] = Field(default_factory=dict)
    # You could also add custom_factories here
    