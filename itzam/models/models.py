from pydantic import BaseModel, Field

class Provider(BaseModel):
  name: str

class Model(BaseModel):
  name: str
  tag: str
  deprecated: bool
  hasVision: bool
  hasReasoningCapability: bool
  isOpenSource: bool
  contextWindowSize: int
  inputPerMillionTokenCost: float
  outputPerMillionTokenCost: float
  provider: Provider