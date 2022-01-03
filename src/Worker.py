from dataclasses import dataclass

from Person import Person

@dataclass
class Worker(Person):

    _salary: float
    _weekly_work: float


    @property
    def salary(self) -> float:
        return self._salary

    
    @property
    def weekly_work(self) -> float:
        return self._weekly_work


    @salary.setter
    def salary(self, x: float) -> None:
        self._salary = x


    @weekly_work.setter
    def weekly_work(self, x: float) -> None:
        self._weekly_work = x

  