import classes as cls


st1 = cls.student.Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = cls.student.Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = cls.group.Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None

gr.delete_student('Taylor')
print(gr)  # Only one student
