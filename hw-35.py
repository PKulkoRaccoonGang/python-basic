class GroupOverflowError(Exception):
    def __init__(self, message='Group overflow (more than 10 students)'):
        self.message = message
        super().__init__(self.message)


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age} years old, {self.gender}'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age} years old, {self.gender}, record book: {self.record_book}'


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, target_student):
        if len(self.group) >= 10:
            raise GroupOverflowError()
        self.group.add(target_student)

    def delete_student(self, last_name):
        target_student = self.find_student(last_name)
        if target_student:
            self.group.remove(target_student)

    def find_student(self, last_name):
        for target_student in self.group:
            if target_student.last_name == last_name:
                return target_student
        return None

    def __str__(self):
        all_students = '\n'.join([str(student) for student in self.group])
        return f'Number: {self.number}\n{all_students}'


students_data = [
    ('Male', 30, 'Steve', 'Jobs', 'AN142'),
    ('Female', 25, 'Liza', 'Taylor', 'AN145'),
    ('Male', 28, 'John', 'Smith', 'AN147'),
    ('Female', 24, 'Anna', 'Johnson', 'AN149'),
    ('Male', 26, 'David', 'Williams', 'AN151'),
    ('Female', 22, 'Emily', 'Brown', 'AN153'),
    ('Male', 27, 'Michael', 'Jones', 'AN155'),
    ('Female', 23, 'Sophia', 'Miller', 'AN157'),
    ('Male', 29, 'Joseph', 'Davis', 'AN159'),
    ('Female', 21, 'Olivia', 'Garcia', 'AN161'),
    ('Male', 31, 'Daniel', 'Martinez', 'AN163')  # 11
]

gr = Group('PD1')

for student_data in students_data:
    student = Student(*student_data)
    gr.add_student(student)

print(gr)
