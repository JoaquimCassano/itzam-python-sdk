from pydantic import BaseModel, Field
from ..text import ResponseMetadata

class Response(BaseModel):
    """
    Represents the response from the object generation API.
    """
    metadata: ResponseMetadata = Field(description="Metadata about the generation process")
    object: dict = Field(description="The generated object based on the schema provided")