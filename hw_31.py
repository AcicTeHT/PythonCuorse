

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.gender} {self.age} {self.first_name} {self.last_name}"
class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return super().__str__() + f" {self.record_book}"



class ErrorIntegerInGroup(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
class Group:
    max_students = 10
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, last_name):
        delete_student = self.find_student(last_name)
        if delete_student:
            self.group.remove(delete_student)
        else:
            print(f"Студента {last_name} немає в групі")

    def find_student(self, last_name):
        for item in self.group:
            if item.last_name == last_name:
                return item
            return None

    def __str__(self):
        students_list = '\n'.join(str(student) for student in self.group)
        return f'Group Number: {self.number}\nStudents:\n{students_list}'



st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None

gr.delete_student('Taylor')
print(gr) # Only one student
