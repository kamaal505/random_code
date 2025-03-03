class Vehicle:
    """
    A base class representing a generic vehicle.
    """

    def __init__(self, brand: str):
        """
        Initialize the Vehicle with a brand.

        Parameters:
        brand (str): The brand of the vehicle.
        """
        self.brand = brand

    def move(self) -> str:
        """
        Describe how the vehicle moves.

        Returns:
        str: A description of the vehicle's movement.
        """
        return "This vehicle moves."


class Car(Vehicle):
    """
    A class representing a car, inheriting from Vehicle.
    """

    def __init__(self, brand: str, doors: int):
        """
        Initialize the Car with a brand and number of doors.

        Parameters:
        brand (str): The brand of the car.
        doors (int): The number of doors the car has.
        """
        super().__init__(brand)
        if doors <= 0:
            raise ValueError("Number of doors must be a positive integer.")
        self.doors = doors

    def move(self) -> str:
        """
        Describe how the car moves.

        Returns:
        str: A description of the car's movement.
        """
        return "The car drives on roads."


class Motorcycle(Vehicle):
    """
    A class representing a motorcycle, inheriting from Vehicle.
    """

    def move(self) -> str:
        """
        Describe how the motorcycle moves.

        Returns:
        str: A description of the motorcycle's movement.
        """
        return "The motorcycle rides on two wheels."


class ElectricCar(Car):
    """
    A class representing an electric car, inheriting from Car.
    """

    def __init__(self, brand: str, doors: int, battery_capacity: str):
        """
        Initialize the ElectricCar with a brand, number of doors, and battery capacity.

        Parameters:
        brand (str): The brand of the electric car.
        doors (int): The number of doors the electric car has.
        battery_capacity (str): The battery capacity of the electric car.
        """
        super().__init__(brand, doors)
        self.battery_capacity = battery_capacity

    def move(self) -> str:
        """
        Describe how the electric car moves.

        Returns:
        str: A description of the electric car's movement.
        """
        return "The electric car moves silently."


# Testing the hierarchy
vehicles = [
    Vehicle("Generic"),
    Car("Toyota", 4),
    Motorcycle("Harley"),
    ElectricCar("Tesla", 4, "100 kWh")
]

for v in vehicles:
    print(f"{v.brand}: {v.move()}")