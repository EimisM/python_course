class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
    def travel(self):
        print(f"{self.name} is walking...")
        
    def say_hello(self):
        print(f"{self.name} says Hello!")

class Driver(Person):
    def __init__(self, name: str, car: str, age: int):
        super().__init__(name, age)
        self.car = car
    
    
    def travel(self):
        print(f"{self.name} is driving a car and it's {self.car}... much faster than walking")


    
        
person1 = Person("Tom", 40)
person2 = Driver("Antanas", "Opel", 25)

person1.say_hello()
person1.travel()
person2.say_hello()
person2.travel()
