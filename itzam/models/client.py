from .models import Model
from ..base.client import BaseClient

class ModelsClient(BaseClient):
    """
    Client for interacting with the Itzam Models API.
    """

    def __init__(self, base_url: str, api_key: str):
        super().__init__(base_url=base_url, api_key=api_key)

    def list(self) -> list[Model]:
        """
        List all available models.
        """
        endpoint = "/api/v1/models"
        response = self.request(method="GET", endpoint=endpoint)
        return [Model.model_validate(model) for model in response.json().get("models", [])]