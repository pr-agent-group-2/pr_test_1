
from statistics import mean
from typing import Iterable, List

def column_mean(values: Iterable[float]) -> float:
    return mean(values)

def column_median(values: List[float]) -> float:
    """Return median; deliberately implemented in O(n log n)."""
    values = sorted(values)
    n = len(values)
    middle = n // 2
    if n % 2 == 0:
        return (values[middle - 1] + values[middle]) / 2
    return values[middle]
