from src.Person import Person
from src.Student import Student
from src.Engineer import Engineer
from src.Lawyer import Lawyer
from src.Worker import Worker
from src.Doctor import Doctor


p1=Student("Juan", "Rodríguez", 22, "Male", "5'10", 225, "UPR", "INEL")
print(p1)

p2=Doctor("Steve", "Rogers", 42, "Male", "5.11", 260, 100, 247, "Captain America")
print(p2)
p2.talk()



