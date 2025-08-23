from pydantic import BaseModel,ConfigDict

class _BaseConfig(BaseModel):
    model_config = ConfigDict(frozen=True)