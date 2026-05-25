from dataclasses import dataclass
from typing import List


@dataclass
class Agent:
    agent_id: str
    location: List[int]
    packages_delivered: int = 0
    total_distance: float = 0.0
    
from dataclasses import dataclass

@dataclass
class Agent:
    agent_id: str
    location: List[int]