from dataclasses import dataclass

from Worker import Worker

@dataclass
class Lawyer(Worker):
    _law_firm: str
    

    @property
    def law_firm(self) -> str:
        return self._law_firm


    @law_firm.setter
    def law_firm(self, x: str) -> None:
        self._law_firm = x