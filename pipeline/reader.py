
import csv
from pathlib import Path
from typing import Dict, Iterator

def read_csv(path: str | Path) -> Iterator[Dict[str, str]]:
    """Yield rows of a CSV file as dicts."""
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row
