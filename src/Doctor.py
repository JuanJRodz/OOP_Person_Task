
"""

Modules used in this project: 'dataclasses'.

Importing from 'Worker' subclass
  
"""


from dataclasses import dataclass, field
from src.Person import Person

from src.Worker import Worker

@dataclass
class Doctor(Worker):
    """Class Doctor() defined.

    Decorators: '@property' and '@x.setter', 
    
    Attributes: {_type
    }
    
    Method defiend: 'talk()' 
    """
    
    
    _type: str
    _doctor_order: float = field(init=False, repr= False)

    @property
    def type(self) -> str:
        return self._type
    
    
    @property
    def doctor_count(self) -> float:
        return self._doctor_order
    

    @type.setter
    def type(self, x: str) -> None:
        self._type = x

    
    def talk(self):
        """Method talk(), prints out a statement with the attributes
        assigend before hand.
        
        """
        print('Hello! I am {} {}. I am a {} doctor that works {} a week and I \
            have a salary of {}.'.format(self._first_name, self._last_name,   \
                                        self._type, self._weekly_hours,
                                        self._salary))


    count = 1
    
    def __post_init__(self):
        self._doctor_order = Doctor.count
        self._worker_order = Worker.count
        self._person_order = Person.count
        Person.count += 1
        Worker.count += 1
        Doctor.count += 1