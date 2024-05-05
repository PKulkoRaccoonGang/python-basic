from .human import Human


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age} years old, {self.gender}, record book: {self.record_book}'

    def __eq__(self, other):
        if isinstance(other, Student):
            return str(self) == str(other)
        return False
