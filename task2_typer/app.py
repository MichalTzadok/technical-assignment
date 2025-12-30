import json
import typer
from typing import Dict, Any, List
from datetime import datetime
import os

app = typer.Typer()
DATA_FILE = "data.json"

def read_data() -> List[Dict[str, Any]]:
    """Read data from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def write_data(data: List[Dict[str, Any]]):
    """Write data to the JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@app.command()
def add(name: str, age: int):
    """
    Add a JSON item to the file with a timestamp.
    """
    data = read_data()
    entry = {
        "timestamp": datetime.now().isoformat(),
        "name": name,
        "age": age
    }
    data.append(entry)
    write_data(data)
    typer.echo(f"Added: {entry}")

@app.command()
def last():
    """
    Show the last 10 items from the file.
    """
    data = read_data()
    last_items = data[-10:]
    typer.echo(last_items)

if __name__ == "__main__":
    app()
