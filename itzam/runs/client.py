from .models import Run
from ..base.client import BaseClient

class RunsClient(BaseClient):
    """
    Client for interacting with the Itzam Runs API.
    """

    def __init__(self, base_url: str, api_key: str):
        super().__init__(base_url=base_url, api_key=api_key)

    def get(self, run_id: str) -> Run:
        """
        Get a run by its ID.
        """
        endpoint = f"/api/v1/runs/{run_id}"
        response = self.request(method="GET", endpoint=endpoint)
        return Run.model_validate(response.json())