from pydantic import BaseModel, Field

class Thread(BaseModel):
    name: str | None = Field(default=None, description="The name of the thread (optional, will auto-generate if not provided)")
    lookup_keys: list[str] | None = Field(default=None, description="Optional lookup keys for finding the thread later", alias="lookupKeys")
    context_slugs: list[str] | None = Field(default=None, description="Optional context slugs to append the context to the thread", alias="contextSlugs")
    created_at: str | None = Field(default=None, description="The date and time when the thread was created", alias="createdAt")
    updated_at: str | None = Field(default=None, description="The date and time when the thread was last updated", alias="updatedAt")
    id: str = Field(..., description="The unique identifier for the thread")


