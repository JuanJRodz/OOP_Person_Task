from dataclasses import dataclass

from Person import Person

@dataclass
class Student(Person):
    institution: str
    major: str
    
    #def __init__(self, fname, lname, age, gender, height, weigth):
    #    super().__init__(fname, lname, age, gender, height, weigth)

    def talk(self, fname, lname, institution, major):
        return 'Hello! I am {} {}. I am a student at {}, studying {}.'.format(fname, lname, institution, major)

p1=Student("María","Rodz", 22, "Female", 5.11, 140, "UPR", "ININ")

talk(p1)
