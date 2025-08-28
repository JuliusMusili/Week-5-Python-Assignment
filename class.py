# Assignment 1
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = 100  # percentage

    def make_call(self, contact):
        print(f"{self.model} is calling {contact}...")

    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        print(f"{self.model} charged. Battery at {self.battery}%")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.storage}GB, Battery: {self.battery}%)"


class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, cooling_system):
        super().__init__(brand, model, storage)
        self.cooling_system = cooling_system

    def play_game(self, game):
        if self.battery > 10:
            print(f"Playing {game} on {self.model} (Cooling: {self.cooling_system})")
            self.battery -= 10
        else:
            print(f"Battery too low to play {game}!")

    def charge(self, amount):  # polymorphism
        super().charge(amount)
        print(f"Fast charging enabled on {self.model}!")


# Example usage
phone1 = Smartphone("Apple", "iPhone 15", 256)
gaming_phone = GamingPhone("Asus", "ROG Phone 7", 512, "Liquid Cooling")

print(phone1)
phone1.make_call("Alice")
phone1.charge(20)

print("\n--- Gaming Phone ---")
print(gaming_phone)
gaming_phone.play_game("PUBG Mobile")
gaming_phone.charge(50)

# Assignment 2
class Vehicle:
    def move(self):
        pass  # abstract-like method


class Car(Vehicle):
    def move(self):
        print("Driving [CAR]")


class Plane(Vehicle):
    def move(self):
        print("Flying [PLANE]")


class Boat(Vehicle):
    def move(self):
        print("Sailing [BOAT]")


# Example usage
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()


