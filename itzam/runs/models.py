from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from ..text.models import ModelInput as Model, Attachment


class AttachmentResponse(Attachment):
  id: str


class Knowledge(BaseModel):
  id: str
  title: str
  url: str
  type: str


class Run(BaseModel):
  id: str
  origin: str
  status: str
  input: str
  output: str
  prompt: str
  input_tokens: int = Field(alias="inputTokens")
  output_tokens: int = Field(alias="outputTokens")
  cost: str
  duration_in_ms: int = Field(alias="durationInMs")
  thread_id: str|None = Field(alias="threadId", default=None)
  model: Model
  attachments: List[Attachment] = Field(default=[])
  knowledge: List[Knowledge ] = Field(default=[])
  workflow_id: str = Field(alias="workflowId")
  created_at: datetime = Field(alias="createdAt")