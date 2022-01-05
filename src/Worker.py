
"""

Modules used in this project: 'dataclasses'.

Importing from 'Persom' abstract class
  
"""


from dataclasses import dataclass

from src.Person import Person

@dataclass
class Worker(Person):
    """Class Worker() defined.

    Decorators: '@property' and '@x.setter', 
    
    Attributes: {_salary,
                _weekly_hours 
    }
    
    Method defiend: 'talk()' 
    """

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
        """Method talk(), prints out a statement with the attributes
        assigend before hand.
        
        """
        print('Hello! I am {} {}. I am a worker that works {} a week and I \
            have a salary of {}.'.format(self._first_name, self._last_name,\
                                        self._weekly_hours, self._salary))

    