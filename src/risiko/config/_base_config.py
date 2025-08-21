from pydantic import BaseModel, Field, ConfigDict

class _BaseConfig(BaseModel):
    model_config = ConfigDict(frozen=True)