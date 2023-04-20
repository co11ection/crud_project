from models import Person, Teacher, Student, Group


def crud():
    global group
    choose = input('Выберите что хотите добавить (1: Группы, 2: Учитель, 3: Студенты, 4: Получить информацию):')
    
    if int(choose) == 1:
        group_name = input("Введите название группу: ")
        group = Group(group_name)
    
    elif int(choose) == 2:
        name = input("Введите имя: ")
        age = input("Введите возраст: ")
        email = input("Введите email: ")
        position = input("Введите позицию: ")
        department = input("Введите кафедру: ")
        teacher = Teacher(name, age, email, position, department)
        group.add_teacher(teacher)
    
    elif int(choose) == 3:
        name = input("Введите имя: ")
        age = input("Введите возраст: ")
        email = input("Введите email: ")
        faculty = input("Введите факультет: ")
        group_name = input("Введите группу: ")
        student = Student(name, age, email, group_name, faculty)
        group.add_student(student)
    elif int(choose) == 4:
        try:
            group.get_info()
        except:
            print('Такой группы нету')
    
    
    crud()

crud()