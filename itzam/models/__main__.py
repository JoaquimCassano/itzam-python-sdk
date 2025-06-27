from .client import ModelsClient

if __name__ == "__main__":
    from rich.console import Console
    from rich.table import Table
    import dotenv,  os
    dotenv.load_dotenv()
    client = ModelsClient(base_url="https://itz.am", api_key=os.getenv("ITZAM_API_KEY"))
    models = client.list()
    console = Console()

    table = Table(title="Models List")
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Tag", style="magenta")
    table.add_column("Deprecated", style="red")
    table.add_column("Open Source", style="green")
    table.add_column("Context Window Size", style="yellow")

    for model in models:
      table.add_row(
        model.name,
        model.tag,
        "Yes" if model.deprecated else "No",
        "Yes" if model.isOpenSource else "No",
        str(model.contextWindowSize)
      )

    console.print(table)