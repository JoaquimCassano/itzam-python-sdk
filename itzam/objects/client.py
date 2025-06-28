from ..base.client import BaseClient
from ..text import Attachment
from .models import Response
import json

class ObjectsClient(BaseClient):
    """
    Client for interacting with the Itzam API's objects endpoint.
    This client provides methods to manage and interact with objects in the Itzam system.
    """

    def __init__(self, base_url: str, api_key: str):
        """
        Initialize the ObjectsClient with the base URL and API key.

        :param base_url: The base URL for the Itzam API.
        :param api_key: The API key for authentication.
        """
        super().__init__(base_url=base_url, api_key=api_key)

    def generate(
        self,
        input: str,
        schema: dict,
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
        endpoint = "/api/v1/generate/object"

        data = {
            "input": input,
            "schema": schema,
        }
        if workflow_slug:
            data["workflowSlug"] = workflow_slug
        if thread_id:
            data["threadId"] = thread_id
        if attachments:
            data["attachments"] = [attachment.model_dump() for attachment in attachments]

        if stream == True:
            return self._stream_object("/api/v1/stream/object", data)
        else:
            response = self.request(method="POST", endpoint=endpoint, data=data)
            return Response.model_validate(response.json())

    def _stream_object(self, endpoint, data):
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
                    elif event.get("type") == "object":
                        yield str(event.get("object"))
                except Exception as e:
                    continue