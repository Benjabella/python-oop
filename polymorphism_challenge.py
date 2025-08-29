"""
Activity 2 – Polymorphism Challenge
Animals and vehicles that share the same interface (`move`)
but behave differently.
"""

class Movable:
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")

class Car(Movable):
    def move(self):
        print("🚗 Driving on the road...")

class Plane(Movable):
    def move(self):
        print("✈️ Flying in the air...")

class Dog(Movable):
    def move(self):
        print("🐕 Running on four legs...")

class Fish(Movable):
    def move(self):
        print("🐟 Swimming in water...")

# Polymorphic runner
def start_journey(movable: Movable):
    movable.move()

# Demo
if __name__ == "__main__":
    movers = [Car(), Plane(), Dog(), Fish()]
    for m in movers:
        start_journey(m)