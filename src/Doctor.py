from dataclasses import dataclass

from Person import Person

@dataclass
class Doctor(Person):
    type: str
