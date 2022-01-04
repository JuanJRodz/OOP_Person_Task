from dataclasses import dataclass

from src.Worker import Worker

@dataclass
class Lawyer(Worker):
    _law_firm: str
    

    @property
    def law_firm(self) -> str:
        return self._law_firm


    @law_firm.setter
    def law_firm(self, x: str) -> None:
        self._law_firm = x

    
    def talk(self):
        print('Hello! I am {} {}. I am a lawyer that works {} a week at {} and I have a salary of {}.'\
            .format(self._first_name, self._last_name, self._weekly_hours, self._law_firm, self._salary))
