from dataclasses import dataclass

from Person import Person

@dataclass
class Worker(Person):
    salary: float
    weekly_work: float

    