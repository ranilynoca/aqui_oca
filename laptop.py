class Laptop:
    def __init__(self, m, b, ra, ro, p):
        self.model = m
        self.brand = b
        self.RAM = ra
        self.ROM_Capacity = ro
        self.processor = p
        
    def change_model(self, m):
        self.model = m
        
    def double_RAM(self):
        self.RAM = self.RAM * 2
        
    def change_brand(self, b):
        self.brand = b
        
    def increase_ROM_capacity(self):
        self.ROM_Capacity = self.ROM_Capacity + 500
        
    def change_processor(self, p):
        self.processor = p


laptop1 = Laptop("MacBookAir", "Apple", 4, 512, "IntelCorei5")
laptop2 = Laptop("ZenBook", "ASUS", 8, 1000, "IntelCorei7")

print("Model before:", laptop1.model)
laptop1.change_model("Zenbook")
print("Model before:", laptop1.model)

print("Brand before:", laptop1.brand)
laptop1.change_brand("ASUS")
print("Brand after:", laptop1.brand)

print("Before double RAM", laptop1.RAM)
laptop1.double_RAM()
print("After double RAM", laptop1.RAM)

print("Before increase ROM_Capacity", laptop1.ROM_Capacity)
laptop1.increase_ROM_capacity()
print("After increaseROM_Capacity", laptop1.ROM_Capacity)

print("Before change processor", laptop1.processor)
laptop1.change_processor("IntelCorei7")
print("After change processor", laptop1.processor)
