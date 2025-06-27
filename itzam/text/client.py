import requests
from .models import (
    Attachment,
    ModelInput,
    ResponseMetadata,
    Response
)
from ..base.client import BaseClient
import json

class TextClient(BaseClient):
    """
    Client for interacting with the Itzam Text API.
    """

    def __init__(self, base_url: str, api_key: str):
        super().__init__(base_url=base_url, api_key=api_key)

    def generate(
        self,
        input: str,
        workflow_slug: str | None = None,
        thread_id: str | None = None,
        attachments: list[Attachment] = None,
        stream: bool = False
    ):
        """
        Generate text using the specified model and prompt.
        If stream=True, returns a generator yielding text deltas.
        """
        if not workflow_slug and not thread_id:
            raise ValueError("Either 'thread_id' or 'worflow_slug' must be provided.")
        endpoint = "/api/v1/generate/text"
        data = {
            "input": input,
            "workflowSlug": workflow_slug,
            **({"threadId": thread_id} if thread_id else {}),
            **({"attachments": [attachment.model_dump() for attachment in attachments]} if attachments else {})
        }

        if stream == True:
            return self._stream_text("/api/v1/stream/text", data)
        else:
            response = self.request(method="POST", endpoint=endpoint, data=data)
            return Response.model_validate(response.json())

    def _stream_text(self, endpoint, data):
        """
        Internal method to handle streaming text responses.
        Yields text deltas as they arrive.
        """
        response = self.request(method="POST", endpoint=endpoint, data=data, stream=True)
        for line in response.iter_lines():
            if line:
                try:
                    event = json.loads(line.decode("utf-8").removeprefix("data: "))
                    if event.get("type") == "text-delta":
                        yield event.get("textDelta")
                except Exception as e:
                    continue