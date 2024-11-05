# create a class called person, with name, age, gender
# has the attributes. have a
# constructor method, normal method and three objects

#Defining a class
class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

#Normal method
    def display(self):
        print(f"I am {self.name}, {self.age} years of age and i'm a {self.gender}")

#Instance of a class /Object
myobj=Person(name="Salmon", age=22, gender="male")
myobj.display()
myobj2=Person(name="Jane", age=20, gender="female")
myobj2.display()
myobj3=Person(name="Jade", age=19, gender="female")
myobj3.display()