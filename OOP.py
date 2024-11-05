#Class
class Fruits:
    #constructor method
    def __init__(self,name,price,color):
        self.name=name
        self.price=price
        self.color=color

        #normal method
    def display(self):
        print(f"I like eating {self.name}, it costs {self.price} and it is {self.color} in color")

#Instance of a class /object
myobj=Fruits(name="Banana", price=50, color="Yellow")
myobj.display()
myobj2=Fruits(name="Watermelon", price=20, color="Red")
myobj2.display()