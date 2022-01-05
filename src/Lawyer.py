
"""

Modules used in this project: 'dataclasses'.

Importing from 'Worker' subclass
  
"""


from dataclasses import dataclass

from src.Worker import Worker

@dataclass
class Lawyer(Worker):
    """Class Lawyer() defined.

    Decorators: '@property' and '@x.setter', 
    
    Attributes: {_law_firm
    }
    
    Method defiend: 'talk()' 
    """
    _law_firm: str
    

    @property
    def law_firm(self) -> str:
        return self._law_firm


    @law_firm.setter
    def law_firm(self, x: str) -> None:
        self._law_firm = x

    
    def talk(self):
        """Method talk(), prints out a statement with the attributes
        assigend before hand.
        
        """
        print('Hello! I am {} {}. I am a lawyer that works {} a week at {} and\
            I have a salary of {}.'.format(self._first_name, self._last_name,
                                        self._weekly_hours, self._law_firm,
                                        self._salary))
