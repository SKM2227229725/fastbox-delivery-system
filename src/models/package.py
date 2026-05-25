from dataclasses import dataclass
from typing import List


@dataclass
class Package:
    package_id: str
    warehouse_id: str
    destination: List[int]
    
from dataclasses import dataclass

@dataclass
class Package:
    package_id: str
    warehouse_id: str
    destination: List[int]