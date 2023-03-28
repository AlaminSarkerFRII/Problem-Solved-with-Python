# method overriding in python

class Phone:

    def __init__(self):
        print("you can send a message from class ")


class Samsung(Phone):  # inherite Phone class by child
    def __init__(self): # overridden here bcz which already has this line 5
        print("you can send a message from Samsung class ")


p = Samsung()

