from dataclasses import dataclass

from Person import Person
from Worker import Worker

@dataclass
class Doctor(Worker):
    _type: str

    @property
    def type(self) -> str:
        return self._type
    
    @type.setter
    def type(self, x: str) -> None:
        self._type = x

# p2=Doctor("Luis", "Tron", "33", "Male", 5.04, 135, 30000, 42, "Dentist")
# print(p2)

# p2.type = "Surgeon"
# print(p2.type)
# print(p2)