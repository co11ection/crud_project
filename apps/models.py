class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

class Teacher(Person):
    def __init__(self, name, age, email, position, department):
        super().__init__(name, age, email)
        self.position = position
        self.department = department

class Student(Person):
    def __init__(self, name, age, email, group, faculty):
        super().__init__(name, age, email)
        self.group = group
        self.faculty = faculty

class Group:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teacher = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def add_teacher(self, teacher):
        self.teacher.append(teacher)

    def remove_teacher(self):
        self.teacher = None

    def get_info(self):
        print("Group:", self.name)
        if self.teacher:
            print("Teacher:", self.teacher.name)
        else:
            print("Teacher: None")
        print("Students:")
        for student in self.students:
            print(student.name)









