class Person :
    cllgName = "MSU"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    # Instance method
    def show(self):
        print(f"Hello {self.name} you are {self.age} years old and you are in {self.cllgName} !")

    def changeAge(self,newAge):
        self.age = newAge
        self.show()

    # Class method
    @classmethod
    def changeCllg(cls,newCllg):
        cls.cllgName = newCllg

s1 = Person("Nazil",20)

s1.changeCllg("CHARUSAT")
s1.show()