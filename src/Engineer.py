from dataclasses import dataclass

from Worker import Worker

@dataclass
class Engineer(Worker):
    type: str
    company: str
    has_masters: bool
    has_doctorate: str
    