"""
Subclass of Car.
This adds a "rocket mode" to the car that extends the functionality of the Car class.
"""
from Car import Car

class RocketCar(Car):
    def __init__(self, x, y=0, heading='E'):
        # Don't forget to call the superclass constructor!
        # Try stepping into this with the debugger to see what it does.
        super().__init__(x, y, heading)
        
        # Keep track of whether we are in rocket mode
        # This is specific to RocketCar, and does not apply to Car.
        self._rocket_mode = False

        # Speed constants for rocket and normal modes
        self._ROCKET_SPEED = 5.0
        self._NORMAL_SPEED = 1.0
        self._speed = self._NORMAL_SPEED

        # Print some additional information that's only relevant to RocketCar.
        print(f"Rocket mode: {self._rocket_mode}")

    def toggle_rocket_mode(self):
        """Toggle rocket speed on and off"""
        if self._rocket_mode:
            self._rocket_mode = False
            self._speed = self._NORMAL_SPEED
        else:
            self._rocket_mode = True
            self._speed = self._ROCKET_SPEED

        # Best practice: Always give feedback to the user when performing an action
        print(f"Rocket mode: {self._rocket_mode}")



# Example Usage - uncomment for testing, but not for submission:
rocket_car = RocketCar(0)
rocket_car.move()
rocket_car.toggle_rocket_mode()
rocket_car.move()