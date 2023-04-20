from crud import CRUDmixin, FileMixin

class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

class Teacher(Person, CRUDmixin, FileMixin):
    def __init__(self, name, age, email, position, department, group_name, filename):
        Person.__init__(self, name, age, email)
        FileMixin.__init__(self, filename)
        self.position = position
        self.department = department
        self.group_name = group_name

class Student(Person,FileMixin, CRUDmixin):
    def __init__(self, name, age, email, group_name, faculty, filename):
        Person.__init__(self, name, age, email)
        FileMixin.__init__(self, filename)
        self.group_name = group_name
        self.faculty = faculty

class Group(FileMixin, CRUDmixin):
    def __init__(self, name, filename, students=None, teachers=None):
        FileMixin.__init__(self, filename)
        if teachers or students is None:
            teachers = []
            students = []
        self.name = name
        self.students = students
        self.teachers = teachers

    def add_student(self, student):
        data = self.read()
        for obj in data:
            if obj['name'] == student.group_name:
                self.students.append(student)
                obj['students'].append(student.name)
                self.write(data)
                return True
        return False

    def remove_student(self, student):
        self.students.remove(student)

    def add_teachers(self, teacher):
        data = self.read()
        for obj in data:

            if obj['name'] == teacher.group_name:
                self.teachers.append(teacher)
                obj['teachers'].append(teacher.name)
                self.write(data)
                return True
        return False

    def remove_teacher(self, teacher):
        self.teachers.remove(teacher)


group = Group('py28', 'group.json')
# st = Student("Ilias", '21', "ilias@gmail.com",'py28', 'python',  'student.json')
# st.create(st)
# group.add_student(st)
teacher_1 = Teacher("Ilias", '21', "ilias@gmail.com", 'mentor', 'python', 'py28', 'teachers.json')
teacher_1.create(teacher_1)
group.create(group)
group.add_teachers(teacher_1)





