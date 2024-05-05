from .exeptions import GroupOverflowError


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
