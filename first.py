
class Car:
    def __init__(self,name,color,model,year):
        self.name = name
        self.color = color
        self.model = model
        self.year = year

    def display(self): #Method to display
        print(f"{self.name} {self.color} {self.model} {self.year}")

    def start(self): #Method to start
        print(f"{self.name} is starting")

    def stop(self): #Method to stop
        print(f"{self.name} is stopping")

    def change(self,color): #Method to change
        self.color = color


car2 = Car("BWM",'Blue','MOD1',2008) 
car2.display()
car2.change("Red")
car2.display()



# car2.start()
# car2.stop()
# class/Objects
# constructor
# methods 


# Encapsulation
# Inheritance


# Polymorphism
# Data Abstraction
