from ..base.client import BaseClient
from .models import (
  Thread
)

class ThreadsClient(BaseClient):
    """
    Client for interacting with the Itzam Threads API.
    """

    def __init__(self, base_url: str, api_key: str):
        super().__init__(base_url=base_url, api_key=api_key)

    def create(self, workflow_slug:str, name:str|None = None, lookup_keys:list[str] = [], context_slugs:list[str] = []) -> Thread:
        """
        Create a new thread.
        """
        endpoint = "/api/v1/threads"
        data = {
            "workflowSlug": workflow_slug,
            "name": name,
        }
        if lookup_keys:
            data["lookupKeys"] = lookup_keys
        if context_slugs:
            data["contextSlugs"] = context_slugs
        response = self.request(method="POST", endpoint=endpoint, data=data)
        return Thread.model_validate(response.json())

    def get(self, thread_id: str) -> Thread:
        """
        Get a thread by its ID.
        """
        endpoint = f"/api/v1/threads/{thread_id}"
        response = self.request(method="GET", endpoint=endpoint)
        return Thread.model_validate(response.json())

    def from_workflow(self, workflow_slug: str) -> list[Thread]:
        """
        Get all threads for a specific workflow.
        """
        endpoint = f"/api/v1/threads/workflow/{workflow_slug}"
        response = self.request(method="GET", endpoint=endpoint)
        return [Thread.model_validate(thread) for thread in response.json().get("threads", [])]

    def runs_from_thread(self, thread_id: str) -> list[dict]:
        """
        Get all runs for a specific thread.
        """
        endpoint = f"/api/v1/threads/{thread_id}/runs"
        response = self.request(method="GET", endpoint=endpoint)
        return response.json().get("runs", [])

