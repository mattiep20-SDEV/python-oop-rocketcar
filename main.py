"""
Demonstrates polymorphism and access modifiers in Python.
"""
from Car import Car
from RocketCar import RocketCar

# This function is a polymorphic function that can take any car object
# and call the move method on it. It doesn't "know" what type of car it is,
# it just knows that it has a move method.
def drive_car(car: Car):
    car.move()
    car.turn_left()
    car.move()
    car.move()
    car.turn_right()
    car.move()  
    car.move()


def main():
    # Create a regular car
    print("\n=== Regular Car Demo ===")
    car = Car(0.0, 0.0, 'E')
    
    # Create a rocket car and turn on rocket mode
    print("\n=== Rocket Car Demo ===")
    rocket_car = RocketCar(0.0, 0.0, 'E')
    rocket_car.toggle_rocket_mode()

    # Race the cars!
    print("\n=== Race Start: Regular Car ===")
    drive_car(car)
    print("\n=== Race Start: Rocket Car ===")
    drive_car(rocket_car)


main()
