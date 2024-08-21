class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    
    def bark(self):
        print(f"{self.name} is barking")

class Puppy(Dog):
    def __init__(self,name,age,color,energy_level):
        super().__init__(name,age,color)
        self.energy_level = energy_level
    
    def play(self):
        print(f"{self.name} is playing with the energy Level {self.energy_level}..")

print("dog execution")
dog1 = Dog("Tommy",5,"Black")
print(dog1.color)


print("Puppy execution")
Puppy1 = Puppy("Ladoo",10,"White & Black",'High')
print(Puppy1.color)


Puppy2 = ("Moti",5,"Brown",'Low')

        
