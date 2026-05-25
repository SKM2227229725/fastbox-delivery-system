from dataclasses import dataclass
from typing import List


@dataclass
class Warehouse:
    warehouse_id: str
    location: List[int]