from pydantic import BaseModel, Field

class Attachment(BaseModel):
    """
    Represents an attachment in a text message.
    """
    file: str = Field(
        ...,
        description="The file path or URL of the attachment. Either a base64 encoded string or a URL."
    )
    mimetype: str = Field(
        ...,
        description="The MIME type of the attachment, e.g., 'image/png', 'application/pdf'."
    )

class ModelInput(BaseModel):
    """
    Represents a model used for text generation.
    """
    name: str = Field(..., description="The name of the model used for this generation.")
    tag: str = Field(..., description="The tag of the model used for text generation.")

class ResponseMetadata(BaseModel):
    """
    Metadata for the response.
    """
    run_id: str = Field(alias="runId", description="The ID of the run created for this generation")
    cost: str = Field(description="The cost of the generation in USD")
    model: ModelInput
    duration: int = Field( description="The duration of the generation in milliseconds", alias="durationInMs")
    input_tokens: int = Field(alias="inputTokens", description="The number of input tokens used in the generation")
    output_tokens: int = Field(alias="outputTokens", description="The number of output tokens used in this generation")

class Response(BaseModel):
    """
    Represents the response from the text generation API.
    """
    text: str = Field(description="The generated text")
    metadata: ResponseMetadata = Field(description="Metadata about the generation process")