# Itzam python sdk
![itzam logo](https://pbs.twimg.com/profile_banners/1930643525021937664/1749136962/600x200)

## Overview

Itzam Python SDK provides a simple interface to interact with the [Itzam API](https://itz.am) for text generation, thread management, model listing, and run inspection.

## Installation

```bash
pip install itzam
```

## Quick Start

```python
from itzam import Itzam

client = Itzam("your-api-key")
response = client.text.generate(
  workflow_slug="your_workflow_slug",
  input="Hello, Itzam!",
  stream=False
)
print(response.text)
```

## Authentication

You can provide your API key directly or set it as an environment variable:

```bash
export ITZAM_API_KEY=your-api-key
```

Then initialize without arguments:

```python
from itzam import Itzam
client = Itzam()
```

## Features

- **Text Generation**: Generate text using your workflows.
- **Threads**: Create and manage threads for conversations.
- **Models**: List available models and their details.
- **Runs**: Inspect previous runs and their metadata.

## Usage Examples

### Generate Text

```python
response = client.text.generate(
  workflow_slug="your_workflow_slug",
  input="Write a poem about the sea."
)
print(response.text)
```

### Stream Text Generation

```python
for delta in client.text.generate(
  workflow_slug="your_workflow_slug",
  input="Tell me a story.",
  stream=True
):
  print(delta, end="", flush=True)
```

### List Models

```python
models = client.models.list()
for model in models:
  print(model.name, model.tag)
```

### Create a Thread

```python
thread = client.threads.create(
  workflow_slug="your_workflow_slug",
  name="Support Conversation"
)
print(thread.id)
```

### Get a Run

```python
run = client.runs.get("run_id")
print(run.output)
```

## Advanced

You can specify a custom API base URL if needed:

```python
client = Itzam(api_key="your-api-key", base_url="https://itz.am")
```

## Requirements

- Python 3.10+
- `requests`
- `pydantic`
- `rich`
- `python-dotenv` (optional, for environment variable loading)

## License

MIT

---

For more details, see the [API documentation](https://itz.am).