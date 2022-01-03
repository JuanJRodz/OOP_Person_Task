from dataclasses import dataclass

from Worker import Worker

@dataclass
class Engineer(Worker):

    _type: str
    _company: str
    _has_masters: bool
    _has_doctorate: bool

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
        print('Hello! I am {} {}. I am a {} engineer that works {} a week at {} and I have a salary of {}.'\
            .format(self._first_name, self._last_name, self._type, self._weekly_hours, self._company, self._salary))


      


    



