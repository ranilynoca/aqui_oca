# This is the VirtualPet
class VirtualPet:
    def __init__(self, name, species, age, mood, energy):
        self.name = name      # Name of the virtual pet
        self.species = species  # Species of the virtual pet
        self.age = age        # Age of the virtual pet
        self.mood = mood      # Current mood of the virtual pet
        self.energy = energy  # Current energy level of the virtual pet

    def play(self):
        """Simulate playing with the virtual pet, affecting mood and energy."""
        self.mood += 5
        self.energy -= 10
        print(f"{self.name} is having fun playing!")

    def feed(self):
        """Simulate feeding the virtual pet, increasing energy level."""
        self.energy += 15
        print(f"{self.name} enjoyed the delicious meal!")

    def sleep(self):
        """Simulate the virtual pet sleeping, restoring energy."""
        self.energy += 20
        self.mood -= 5
        print(f"{self.name} is taking a nap and recharging!")

    def pet(self):
        """Simulate petting the virtual pet, improving mood."""
        self.mood += 10
        print(f"{self.name} loves the attention!")

    def display_status(self):
        """Display the current status of the virtual pet."""
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Age: {self.age}")
        print(f"Mood: {self.mood}")
        print(f"Energy: {self.energy}")


# Example usage:
if __name__ == "__main__":
    my_pet = VirtualPet("Coco", "Dog", 3, 50, 70)
    
    my_pet.display_status()
    
    my_pet.play()
    my_pet.feed()
    my_pet.pet()
    my_pet.sleep()

    my_pet.display_status()
