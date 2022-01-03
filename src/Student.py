from dataclasses import dataclass

from Person import Person

@dataclass
class Student(Person):
    _institution: str
    _major: str

    
    @property
    def institution(self) -> str:
        return self._institution


    @property
    def major(self) -> str:
        return self._major


    @institution.setter
    def institution(self, x: str) -> None:
        self._institution = x


    @major.setter
    def major(self, x: str) -> None:
        self._major = x


    def talk(self):
        print('Hello! I am {} {}. I am a student at {}, studying {}.'.format(self._first_name, self._last_name, self._institution, self._major))

p1=Student("María","Rodz", 22, "Female", 5.11, 140, "UPR", "ININ")

p1.talk()
