import requests
from ..utils.exceptions import raise_for_status
import logging
logger = logging.getLogger(__name__)
class BaseClient:
    """    Base client for making HTTP requests to the Itzam API.
    This class should be extended by specific API clients.
    It handles the common functionality of making requests, including setting headers and handling errors.
    """
    def __init__(self, api_key: str, base_url: str):
        self.base_url = base_url
        self.api_key = api_key

    def request(self, method: str, endpoint: str, params: dict = None, data: dict = None,  **kwargs):
        url = f"{self.base_url}{endpoint}"
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Itzam-Python-SDK/1.0",
            "Api-Key": self.api_key
        }

        response = requests.request(method, url, headers=headers, params=params, json=data, **kwargs)

        logger.debug(f"Request URL: {response.request.url}")
        logger.debug(f"Request Method: {response.request.method}")
        logger.debug(f"Request Headers: {response.request.headers}")
        logger.debug(f"Request Body: {response.request.body}")
        logger.debug(f"Response Status Code: {response.status_code}")
        logger.debug(f"Response body: {response.text}")

        if response.status_code != 200:
            raise_for_status(response)

        return response