
"""

Modules used in this project: 'dataclasses'.

Importing from 'Worker' subclass
  
"""


from dataclasses import dataclass, field

from src.Worker import Worker


@dataclass
class Engineer(Worker):
    """Class Engineer() defined.

    Decorators: '@property' and '@x.setter', 
    
    Attributes: {_type,
                _company,
                _has_masters,
                _has_doctorate 
    }
    
    Method defiend: 'talk()' 
    """
    _type: str
    _company: str
    _has_masters: bool
    _has_doctorate: bool
    _engineer_order: float = field(init=False, repr= False)

    @property
    def type(self) -> str:
        return self._type
    

    @property
    def company(self) -> str:
        return self._company
    

    @property
    def has_masters(self) -> bool:
        return self._has_masters


    @property
    def has_doctorate(self) -> bool:
        return self._has_doctorate
    
    
    @property
    def engineer_count(self) -> float:
        return self._engineer_order

    
    @type.setter
    def type(self, x: str) -> None:
        self._type = x


    @company.setter
    def company(self, x: str) -> None:
        self._company = x
    

    @has_masters.setter
    def has_masters(self, x: bool) -> None:
        self._has_masters = x  

        
    @has_doctorate.setter
    def has_doctorate(self, x: bool) -> None:
        self._has_doctorate = x 


    def talk(self):
        """Method talk(), prints out a statement with the attributes
        assigend before hand.
        
        """
        print('Hello! I am {} {}. I am a {} engineer that works {} a week at \
            {} and I have a salary of {}.'.format(self._first_name,          
                                            self._last_name, self._type,
                                            self._weekly_hours, self._company, 
                                            self._salary))


    count = 1
    
    def __post_init__(self):
        self._engineer_order = Engineer.count
        Engineer.count += 1
      


    



