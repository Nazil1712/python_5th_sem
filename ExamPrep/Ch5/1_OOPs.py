class Person:
    def __init__(self,name, gender, profession):
        self.name = name
        self.gender = gender
        self.profession = profession

    def show(self):
        print(f"Name : {self.name}, Gender : {self.gender}, Profession : {self.profession}")

    def work(self):
        print(f"{self.name} is working as {self.profession}")


# john = Person("John","male","Web Dev")

# john.work()
# john.show()
# john.gender = "Female"
# john.show()




# Class variable and Instance variable
class Student:
    cllg_name = "MSU"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f"{self.name} is {self.age} years old studying in {Student.cllg_name}")



s1 = Student("Harry",15)
s1.show()


s1.name = "Nazil"
s1.age = 20
Student.cllg_name = "CHARUSAT"

s1.show()