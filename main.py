from src.Person import Person
from src.Student import Student
from src.Engineer import Engineer
from src.Lawyer import Lawyer
from src.Worker import Worker
from src.Doctor import Doctor


p1=Student("María", "Rodz", 14, "Female", "5'6", 95, "UPR", "INEL")
print(p1)
p2=Student("Juan", "Rodz", 21, "Female", "5.11", 225, "UPR", "INEL")
print(p2)
p3=Worker("José", "Rodz", 63, "Male", "5'10", 300, 30000, 0)
print(p3)
p4=Lawyer("Fiona", "Morales", 27, "Female", "5'4", 145, 20000, 247, "Morales'Firm")
print(p4)

print(p1.student_count)
print(p2.student_count)
print(p2.person_count)
print(p4.lawyer_count)
print(p4.person_count)
print(p4.worker_count)

