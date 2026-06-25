


class student:

    def __init__(self, name, major, year, marks):

        self.name = name
        self.major = major
        self.year = year
        self.marks = marks

    def student_marks(self):
        print(f"{self.name} has scored {self.marks} cgpa")

    def student_details(self):
        print(f"student name is {self.name} studying in {self.year} {self.major}")


student1 = student("John","CS", "3rd year", 6.89)
student2 = student("Jack","Mech", "3rd year", 7.2)


student1.student_details()
student2.student_marks()


#above code describes how to make class functions in python 


