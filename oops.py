# Classes and Objects
# Attributes and Methods
# Encapsulation
# Inheritance
# Polymorphism

# Class: A class is a blueprint for the object.
car1Name = "Audi"
car1Model = "Q7"
car1Color = "Black"
car1MaxPrice = 123420
car1MaxSpeed = 260 

car2Name = "BMW"
car2Model = "Q7"
car2Color = "Black"
car2MaxPrice = 123420
car2MaxSpeed = 260 

car1 = {
    "name":"audi",
    "model":"Q7",
    "color":"black",
    "price":123420,
}

car2 = {
    "name":"BMW",
    "model":"Q7",
    "color":"black",
    "price":123420,
}

class Car:
    def __init__(self, name, model, color, price, speed,status="Stopped"):
        self.name = name
        self.model = model
        self.color = color
        self.price = price
        self.__currentSpeed = speed
        self.status = status

    def displayCar(self):
        print("Here is the details of Car")
        print(f"Name: {self.name}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Price: {self.price}")
        print(f"Speed: {self.__currentSpeed}")
        print()

    def changeColor(self,color):
        self.color = color

    def changeStatus(self,status):
        self.status = status
        print("Car status is:-", self.status)

    def accelerate(self,speed):
        self.__currentSpeed += speed
        print("Car speed is:-", self.__currentSpeed)

    def showSpeed(self):
        print("Car speed is:-", self.__currentSpeed)

car1 = Car("Audi", "Q7", "Black", 123420, 60)
car1.changeStatus("Started")
# print(car1.currentSpeed)
car1.showSpeed()
car1.accelerate(20)
car1.showSpeed()









# car2 = Car("BMW", "B7", "Red", 123420, 260)
# car3 = Car("Mercedes", "M7", "Blue", 123420, 260)

# car1.displayCar()
# car1.changeColor('Yellow')
# car1.displayCar()
# print("Car1 status is:-", car1.status)



# car2.displayCar()
# car3.displayCar()

# Object: An object is an instance of a class.
# Attributes: An attribute is a characteristic of an object.
# Methods: A method is an operation we can perform with the object.
# Inheritance: It is a mechanism where a new class inherits properties from an existing class.
# Encapsulation: It is restricting direct access to some of the object's components.
# Polymorphism: It is a concept where one task can be performed in different ways.
