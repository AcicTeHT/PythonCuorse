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
        return f"{self.gender} {self.age} {self.first_name} {self.last_name} {self.record_book}"

class ErrorIntegerInGroup(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
class Group:
    max_students= 10
    def __init__(self, number):
        self.number = number
        self.group = set()
    def __repr__(self):
        return f"Student: "

    def add_student(self, student):
        if len(self.group) >= self.max_students:
            raise ErrorIntegerInGroup("Досягнуто максимальної кількості студентів у групі")
        self.group.add(student)


    def delete_student(self, last_name):
        if last_name in self.group:
            self.group.remove(last_name)

    def find_student(self, last_name):
        for item in self.group:
            if item.last_name == last_name:
                print(item)
                return item
            return None

    def __str__(self):
        all_students = ''
        for item in self.group:
            all_students += f'{str(item)} \n'
        return f'Number:{self.number}\n {all_students} '


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st4 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st5 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st6 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st7 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st8 = Student('Female', 29, 'Anna', 'Maylor', 'AN162')
st9 = Student('Female', 29, 'Anna', 'Maylor', 'AN162')
st10 = Student('Female', 29, 'Anna', 'Maylor', 'AN162')
st11 = Student('Female', 29, 'Anna', 'Maylor', 'AN162')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)
# gr.add_student(st11)
print(gr)
