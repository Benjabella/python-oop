"""
Assignment 1 – Design Your Own Class
A minimal hierarchy that models smart devices with
constructors, attributes, methods, inheritance, and encapsulation.
"""

class SmartDevice:
    """Base class representing any smart device."""
    _id_counter = 1000  # 'protected' class variable for auto-ID

    def __init__(self, brand: str, model: str, price: float):
        self._device_id = SmartDevice._id_counter
        SmartDevice._id_counter += 1
        self.brand = brand
        self.model = model
        self._price = price  # 'protected' attribute (encapsulation)

    # Encapsulation: read-only property for price
    @property
    def price(self) -> float:
        return self._price

    def turn_on(self):
        print(f"{self} is now ON.")

    def turn_off(self):
        print(f"{self} is now OFF.")

    def __str__(self):
        return f"{self.brand} {self.model} (id={self._device_id})"


class Smartphone(SmartDevice):
    """Inherited class with extra attributes and polymorphic behaviour."""
    def __init__(self, brand: str, model: str, price: float, os: str, storage_gb: int):
        super().__init__(brand, model, price)
        self.os = os
        self.storage_gb = storage_gb

    def install_app(self, app_name: str):
        print(f"Installing '{app_name}' on {self}")

    # Polymorphism: override parent's turn_on
    def turn_on(self):
        super().turn_on()
        print("Booting OS...")

    # Additional method
    def take_photo(self):
        print(f"{self} snapped a photo!")


class Smartwatch(SmartDevice):
    """Another inherited class."""
    def __init__(self, brand: str, model: str, price: float, has_gps: bool):
        super().__init__(brand, model, price)
        self.has_gps = has_gps

    def track_workout(self):
        print(f"{self} is now tracking your workout.")


# Quick demo
if __name__ == "__main__":
    phone = Smartphone("Google", "Pixel 9", 899.0, "Android 15", 256)
    watch = Smartwatch("Samsung", "Galaxy Watch 7", 299.0, True)
    phone.turn_on()
    phone.take_photo()
    watch.turn_on()
    watch.track_workout()