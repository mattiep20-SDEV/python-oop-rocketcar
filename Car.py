"""
Car is the base class, or superclass, of all other car classes.
It has a simple interface: a constructor and one "move" method.
"""
# Reminder: 
# "superclass" = "parent class" = "base class"
# "subclass" = "child class"

class Car:
    def __init__(self, x, y=0, heading='E'):
        # Protected attributes (single underscore in Python)
        # These can be used by this class and any child classes,
        # but should not be accessed directly by other code that uses our car.
        self._x = x
        self._y = y
        self._heading = heading
        self._speed = 1.0
        print(f"Car created at position ({self._x}, {self._y})")

    # This is a public method, meant to be called by any other code.
    def move(self):
        """Moves the car forward by its speed"""
        if self._heading == 'E':
            self._x += self._speed
        elif self._heading == 'W':
            self._x -= self._speed
        elif self._heading == 'N':
            self._y += self._speed
        elif self._heading == 'S':
            self._y -= self._speed
        else:
            print(f"Unknown heading '{self._heading}', not moving.")
        print(f"Position: {self._x}, {self._y} | Heading: {self._heading}")
        
    def turn_left(self):
        """Turns the car left (counterclockwise)"""
        directions = ['N', 'W', 'S', 'E']
        current_index = directions.index(self._heading)
        self._heading = directions[(current_index + 1) % len(directions)]
        print(f"Turned left. New heading: {self._heading}")

    def turn_right(self):
        """Turns the car right (clockwise)"""
        directions = ['N', 'E', 'S', 'W']
        current_index = directions.index(self._heading)
        self._heading = directions[(current_index + 1) % len(directions)]
        print(f"Turned right. New heading: {self._heading}")

        print(f' Turning right')

# # Example Usage - uncomment for testing
car = Car(0.0, 0.0, 'E')
car.move()
car.turn_left()
car.move()
car.turn_right()
car.move()