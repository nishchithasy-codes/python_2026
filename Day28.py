class student:
    def __init__(self,roll_no,name):
        self.roll_no = roll_no
        self.name = name
        self.__marks = {}

    def get_marks(self):
        return self.__marks
    
    def add_marks(self,subject,marks):
        self.__marks[subject] = marks

    def calculate_average(self):
        total = 0
        for mark in self.__marks.values():
            total += mark
        average = total / len(self.__marks)
        return average
    
    def is_passed(self):
        has_passed = all(mark<35 for mark in self.__marks.values())
        if has_passed:
            print(f"{self.name} has passed.")
        else:
            print(f"{self.name} has failed.")

    def calculate_grade(self):
        print("Grade:",end = "")
        percentage = self.calculate_average()*100
        if percentage >= 95:
            print("Grade>>> A")
        elif percentage >= 85:
            print("Grade>>> B")
        else:
            print("Grade>>> C")

class ReportCard:
    @staticmethod           #no needs of objects
    def generate_report(student:student):
        student_marks = student.get_marks()
        print(f"{student.name}")
        print(f"Roll no: {student.roll_no}")
        print("-----------------marks-------------------")
        for subject,marks in student_marks.items():
            print(f"{subject} >> {marks}")
        print("-----------------------------------------")
        print(f"Average marks={student.calculate_average()}")
        student.is_passed()
        student.calculate_grade()

class ClassRoom:
    def __init__(self,grade,section):
        self.grade = grade
        self.section = section
        self.__students = []

    def add_students(self,student):
        self.__students.append(student)
    
    def calculate_class_average(self):
        pass

    def get_students_list(self):
        for student in (self.__students):
            print(f"{student.roll_no}. {student.name}")


s1 = student(1, "Akash")
s2 = student(2, "Bharath")

s1.add_marks("Maths",95)
s1.add_marks("Science",85)
s1.add_marks("English",34)

s2.add_marks("Maths",99)
s2.add_marks("Science",79)
s2.add_marks("English",35)

s1.calculate_average()
s1.calculate_grade()
s1.is_passed()

s2.calculate_average()
s2.calculate_grade()
s2.is_passed()

ReportCard.generate_report(s1)
ReportCard.generate_report(s2)


c = ClassRoom("10th","B")
c.add_students(s1)
c.add_students(s2)
c.get_students_list()

