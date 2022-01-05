
"""

Modules used in this project: 'dataclasses'.

Importing from 'Persom' abstract class
  
"""


from dataclasses import dataclass

from src.Person import Person

@dataclass
class Student(Person):
    """Class Student() defined.

    Decorators: '@property' and '@x.setter', 
    
    Attributes: {_institution,
                _major 
    }
    
    Method defiend: 'talk()' and 'calculate()' 
    """
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
        """Method talk(), prints out a statement with the attributes
        assigend before hand.
        
        """
        print('Hello! I am {} {}. I am a student at {}, studying {}.'\
            .format(self._first_name, self._last_name, self._institution,
                    self._major))

    def calculate(self, *grades):
        """Method calculate(), calculates the average of the values inputed by
        the user.
        
        Variable : *grades
        """
        final_grade = sum(grades)/ len(grades) 
        print('The students final grade is: ', final_grade)

    # def pcounter(count):
    #     count = 1 + count
    #     print (count)

# Student.pcounter(1)


