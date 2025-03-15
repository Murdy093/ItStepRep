class Human:
    def __init__(self, name = None, age = 0, stat = None):
        self.name = name
        self.age = age
        self.stat = stat
    def GetInfo(self):
        print(f"Name is {self.name}. Age is {self.age}. Stat is {self.stat}")
    def Talk(self):
        print("Hello, I'm Human")

obj = Human("Roman", 20, "M")
obj1 = Human("Nastya", 20, "F")
obj.GetInfo()
obj1.GetInfo()
objg = Human()
objg.GetInfo()
