from abc import abstractmethod
from abc import ABC
from dataclasses import dataclass

@dataclass
class Person(ABC):

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
        pass

# p1=Person("María","Rodz", 22, "Female", 5.11, 140)

# print(p1)

# p1.first_name = "Juan"
# print(p1.first_name)
# print(p1)

# p1.last_name = "Rivera" 
# print(p1.last_name) #??
# print(p1)

# p1.weight = 200
# print(p1.weight)
# print(p1)

# p1._weight = 300
# print(p1._weight)
# print(p1)




