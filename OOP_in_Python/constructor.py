# constructor in python

class Student:
    roll = "",
    gpa = "",

    # define a constructor method which don't need to call
    def __init__(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

    # define a function or method

    def display(self):
        print(f" Roll : {self.roll} , GPA: {self.gpa}")


# create object -01


rahim = Student(1200, 3.02)
rahim.display()

# create object -02

kahim = Student(10210, 3.00)
kahim.display()
