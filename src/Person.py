
"""
The objective of this proyect is to implement Object Oriented Programing to
construct varies objects with Inheritence as its main focus.

Modules used in this project: 'abc' and 'dataclasses'.
  
"""


from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass


@dataclass
class Person(ABC):
    """Abstract Class Person(), will set every attribute that will be used in 
    the other subclasses.

    Decorators: '@property' and '@x.setter', 
    
    Attributes: {_first_name,
                 _last_name,
                 _age,
                 _gender,
                 _heigth,
                 _weight
    }
    
    Abstract Method defiend: 'talk()' 
    """
    

    _first_name: str 
    _last_name: str 
    _age: float 
    _gender: str 
    _height: str
    _weight: float 

    
    @property
    def first_name(self) -> str:
        return self._first_name
    

    @property
    def last_name(self) -> str:
        return self._last_name


    @property
    def age(self) -> float:
        return self._age


    @property
    def gender(self) -> str:
        return self._gender


    @property
    def height(self) -> float:
        return self._height


    @property
    def weight(self) -> float:
        return self._weight
    

    @first_name.setter
    def first_name(self, x: str) -> None:
        self._first_name = x
    

    @last_name.setter
    def last_name(self, x: str) -> None:
        self._last_name = x
    

    @age.setter
    def age(self, x: float) -> None:
        self._age = x
    
    
    @gender.setter
    def gender(self, x: str) -> None:
        self._gender = x
    

    @height.setter
    def height(self, x: float) -> None:
        self._height = x
    

    @weight.setter
    def weight(self, x: float) -> None:
        self._weight = x
    
    @abstractmethod
    def talk(self):
        """Method talk(), will prints out a statement with the attributes
        assigend before hand.
        
        """
        pass


