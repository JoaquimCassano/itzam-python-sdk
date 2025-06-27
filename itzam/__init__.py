"""
The Python sdk for the Itzam API.
Example usage:

```python
from itzam import Itzam

client = Itzam("your api key")
response = client.text.generate(
    workflow_slug="your_workflow_slug",
    input="your input text",
    stream=False
)
print(response.text)
```
"""
from .text.client import TextClient
from .threads import ThreadsClient
from .runs import RunsClient
from .models import ModelsClient
import dotenv, os

class Itzam:
  def __init__(self, api_key: str|None = None, base_url: str="https://itz.am"):
    """
    Initialize the Itzam SDK with the base URL and API key. If no API key is provided, it will look for the `ITZAM_API_KEY` environment variable.

    :param base_url: The base URL for the Itzam API.
    :param api_key: The API key for authentication.
    """
    if not api_key:
      dotenv.load_dotenv()
      api_key = os.getenv("ITZAM_API_KEY")
      if not api_key:
        raise ValueError("API key is required. Please provide it as an argument or set the ITZAM_API_KEY environment variable.")

    self.text = TextClient(base_url=base_url, api_key=api_key)
    self.threads = ThreadsClient(base_url=base_url, api_key=api_key)
    self.runs = RunsClient(base_url=base_url, api_key=api_key)
    self.models = ModelsClient(base_url=base_url, api_key=api_key)