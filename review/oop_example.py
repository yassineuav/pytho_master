
# Define a class called "Car"
class Car:
    # Constructor method to initialize the object
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0  # Initial speed is 0

    # Method to start the car
    def start(self):
        print(f"{self.year} {self.make} {self.model} is starting.")

    # Method to accelerate the car
    def accelerate(self, mph):
        self.speed += mph
        print(f"The car is now going {self.speed} mph.")

    # Method to brake the car
    def brake(self, mph):
        self.speed -= mph
        print(f"The car is now going {self.speed} mph.")

# Create instances of the Car class
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Ford", "Mustang", 2023)

# Use methods to interact with the objects
car1.start()
car1.accelerate(30)
car1.brake(10)

car2.start()
car2.accelerate(50)
car2.brake(20)
