from dataclasses import dataclass

from Worker import Worker

@dataclass
class Lawyer(Worker):
    law_firm: str
    