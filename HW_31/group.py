
import student
import TooManyStudentsError


class Group:
    max_students = 10
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= self.max_students:
            raise TooManyStudentsError.TooManyStudentsError("Досягнуто максимальної кількості студентів у групі")
        self.group.add(student)


    def delete_student(self, last_name):
        delete_student = self.find_student(last_name)
        if delete_student:
            self.group.remove(delete_student)
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
