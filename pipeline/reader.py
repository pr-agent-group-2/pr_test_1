
import csv
import json
from pathlib import Path
from typing import Dict, Iterator, Any

def read_csv(path: str | Path) -> Iterator[Dict[str, str]]:
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row

def read_json(path: str | Path) -> Iterator[Dict[str, Any]]:
    """New helper: stream rows from a JSON list file."""
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
        if isinstance(data, list):
            for obj in data:
                yield obj
        else:
            raise ValueError("JSON root must be a list")
