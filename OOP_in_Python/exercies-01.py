# Solve the Problem Using constructor in python

#Triangle -> base , height , calculated

class Triangle:
    base = ""
    height = ""

    # define a constructor method which don't need to call
    def __init__(self, base, height):
        self.base = base
        self.height = height

    # define a function or method

    def calculated_area(self):
        area = 0.5 * self.base * self.height
        print(f"The Area is {area}")


# create object -01


t1 = Triangle(10, 5)
t1.calculated_area()

# create object -02

t2 = Triangle(10, 10)
t2.calculated_area()
