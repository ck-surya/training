
class Car:
    def play(self):
        print("Car is running")
    
    def stop(self):
        print("Car is stopped")

class Bike:
    def play(self):
        print("Bike is running")
    
    def stop(self):
        print("Bike is stopped")

class Bubble_Shooter:
    def play(self):
        print("asdfasndlk")

    def stop(self):
        pass

def play_toy(obj):
    obj.play()

my_car = Car()
play_toy(my_car,False)

my_bike = Bike()
play_toy(my_bike)

my_car.play()
my_bike.play()




