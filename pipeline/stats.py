
from statistics import mean
from typing import Iterable

def column_mean(values: Iterable[float]) -> float:
    """Return the arithmetic mean of a collection of floats."""
    return mean(values)
