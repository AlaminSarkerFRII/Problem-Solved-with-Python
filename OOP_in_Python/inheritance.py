class Phone:

    def Message(self):
        print("you can send a message")

    def Call(self):
        print("you can send a call")


class Samsung(Phone):  # inherite Phone class by child

    def Photo(self):
        print("you can send a photo")


p = Samsung()
p.Call()
p.Message()
p.Photo()
