class Vehicle:
    def __init__(self, make, model, year, current_speed, colour):
        self.make = make
        self.model = model
        self.year = year
        self.current_speed = current_speed
        self.colour = colour


    def move(self): 
        """Move the vehicle."""
        print(f"The {self.year} {self.make} {self.model} is moving.")

    def stop(self):
        """Stop the vehicle."""
        self.current_speed = 0
        print(f"The {self.year} {self.make} {self.model} has stopped.")

    def describe(self):
        """Describe the vehicle."""
        print(f"\n{self.year} {self.make} {self.model} - Colour: {self.colour}, Current Speed: {self.current_speed} km/h")


class Car(Vehicle):
    '''A class representing a car, inheriting from Vehicle.'''	
    def __init__(self, make, model, year, current_speed, colour, doors):
        super().__init__(make, model, year, current_speed, colour)
        self.doors = doors
    
    def move(self):
        """Override the move method for cars."""
        self.current_speed = min(65, self.max_speed)
        print(f"The {self.year} {self.make} {self.model} is driving on the road.")

    def stop(self):

        self.current_speed = 0
        self.stop()
        print(f"The {self.year} {self.make} {self.model} has stopped at the traffic light.")

    def describe(self):
        super().describe()
        print(f"Number of doors: {self.doors}")

    def honk(self):
        print(f"The {self.year} {self.make} {self.model} honks: Beep! Beep!")

class Boat(Vehicle):
    ''' A class representing a boat, inheriting from Vehicle.'''
    def __init__(self, make, model, year, current_speed, colour, length):
        super().__init__(make, model, year, current_speed, colour)
        self.length = length

    def move(self):
        self.current_speed = min(30, self.max_speed)
        print(f"The {self.year} {self.make} {self.model} is sailing on the water.")

    def stop(self):
        self.current_speed = 0
        self.stop()
        print(f"The {self.year} {self.make} {self.model} has docked at the harbor.")

    def describe(self):
        super().describe()
        print(f"Length: {self.length} meters")

    def anchor(self):
        print(f"The {self.year} {self.make} {self.model} is anchored.")

class Plane(Vehicle):
    ''' A class representing a plane, inheriting from Vehicle.'''
    def __init__(self, make, model, year, current_speed, colour, wingspan):
        super().__init__(make, model, year, current_speed, colour)
        self.wingspan = wingspan

    def move(self):
        self.current_speed = min(250, self.max_speed)
        print(f"The {self.year} {self.make} {self.model} is flying in the sky.")

    def land(self):
        self.current_speed = 0
        self.stop()
        print(f"The {self.year} {self.make} {self.model} has landed on the runway.")

    def describe(self):
        super().describe()
        print(f"Wingspan: {self.wingspan} meters")


def travel_with_vehicle(vehicle):
    """Function demonstrating polymorphism with different vehicle types."""
    print(f"\nStarting journey with {vehicle.name}:")
    vehicle.move()  # This calls the appropriate move() method based on the object's type
    vehicle.describe()


if __name__ == "__main__":
    # Create different vehicle objects
    sedan = Car("Civic", "Blue", 120, 4)
    yacht = Boat("Serenity", "White", 30, "yacht")
    jet = Plane("Boeing 737", "Silver", 600, 35000)
    
    # Call the same function with different vehicle types
    travel_with_vehicle(sedan)
    travel_with_vehicle(yacht)
    travel_with_vehicle(jet)
    # Call the honk method for the car
    sedan.honk()
    # Call the anchor method for the boat
    yacht.anchor()
    # Call the stop method for the plane
    jet.land()