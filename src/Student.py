from dataclasses import dataclass
from typing import Counter

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
        print('Hello! I am {} {}. I am a student at {}, studying {}.'\
            .format(self._first_name, self._last_name, self._institution, self._major))

    def calculate(self, *grades):
    #    sum_grades = sum(grades)
        final_grade = sum(grades)/ len(grades) 
        print('The students final grade is: ', final_grade)

p1=Student("María","Rodz", 22, "Female", 5.11, 140, "UPR", "ININ")
print(p1)
p1.calculate(32,45,69)
#print(Student.person_counter)
# p1.talk()
