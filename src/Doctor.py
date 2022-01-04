from dataclasses import dataclass

from src.Worker import Worker

@dataclass
class Doctor(Worker):
    _type: str

    @property
    def type(self) -> str:
        return self._type
    

    @type.setter
    def type(self, x: str) -> None:
        self._type = x

    
    def talk(self):
        print('Hello! I am {} {}. I am a {} doctor that works {} a week and I have a salary of {}.'\
            .format(self._first_name, self._last_name, self._type, self._weekly_hours, self._salary))


# p2=Doctor("Luis", "Tron", "33", "Male", 5.04, 135, 30000, 42, "Dentist")
# print(p2)

# p2.type = "Surgeon"
# print(p2.type)
# print(p2)