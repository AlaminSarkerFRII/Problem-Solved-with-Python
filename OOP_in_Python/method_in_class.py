# class with Method or Function in python

class Student:
    roll = "",
    gpa = "",

    # define a function or method for set values
    def set_value(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa

    # define a function or method

    def display(self):
        print(f" Roll : {self.roll} , GPA: {self.gpa}")


# create object -01


rahim = Student()
rahim.set_value(1100, 5.00)
rahim.display()  # call display

# create object -02

kahim = Student()
kahim.set_value(20100, 4.00)
kahim.display()  # call display
