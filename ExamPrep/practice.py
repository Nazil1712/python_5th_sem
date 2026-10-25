class Employee:

    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary


    def show(self):
        print(self.name, self.__salary)


s1 = Employee("Nazil",1)

s1.show()

print(s1.__salary)