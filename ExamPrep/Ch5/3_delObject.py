class Fruit:
    def __init__(self,colour,name):
        self.name = name
        self.colour = colour

    def show(self):
        print(f"Fruit is {self.name} and colour is {self.colour}")


f1 = Fruit("apple","red")
f1.show()

del f1
print(f1.colour)

