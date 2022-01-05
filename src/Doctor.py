
"""

Modules used in this project: 'dataclasses'.

Importing from 'Worker' subclass
  
"""


from dataclasses import dataclass

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

    @property
    def type(self) -> str:
        return self._type
    

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
