from dataclasses import dataclass

from Person import Person

@dataclass
class Worker(Person):

    _salary: float
    _weekly_hours: float


    @property
    def salary(self) -> float:
        return self._salary

    
    @property
    def weekly_hours(self) -> float:
        return self._weekly_hours


    @salary.setter
    def salary(self, x: float) -> None:
        self._salary = x


    @weekly_hours.setter
    def weekly_hours(self, x: float) -> None:
        self._weekly_hours = x


    def talk(self):
        print('Hello! I am {} {}. I am a worker that works {} a week and I have a salary of {}.'\
            .format(self._first_name, self._last_name, self._weekly_hours, self._salary))

  