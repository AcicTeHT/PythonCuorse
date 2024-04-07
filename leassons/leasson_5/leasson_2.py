

class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Ім'я: {self.first_name}, Прізвище: {self.last_name}, Вік: {self.age}, Стать: {self.gender}"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return super().__str__() + f"  {self.record_book}"


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, last_name):
        student_to_delete = self.find_student(last_name)
        if student_to_delete:
            self.group.remove(student_to_delete)
            print(f"Студента {last_name} видалено з групи")
            return
        else:
            print(f"Студента {last_name} немає в групі")

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        students_list = '\n'.join(str(student) for student in self.group)
        return f'Group Number: {self.number}\nStudents:\n{students_list}'

# Приклад використання класів
group1 = Group(1)


student1  = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
student2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

group1.add_student(student1)
group1.add_student(student2)

print(group1)
assert group1.find_student('Jobs') == student1  # 'Steve Jobs'
assert group1.find_student('Jobs2') is None
# Перевірка знаходження студента з прізвищем 'Jobs' у групі
found_student = group1.find_student('Jobs')
assert found_student == student1, "Студент з прізвищем 'Jobs' не знайдений у групі"
