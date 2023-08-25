#This is the StudentID class

class StudentID:
    def __init__(self, n, f, l, d, g):
        self.number = n
        self.first_name = f
        self.last_name = l
        self.date_of_birth = d
        self.grade_level = g
        
    def change_number(self, n):
        self.number = n
        
    def change_first_name(self, f):
        self.first_name = f
        
    def change_last_name(self, l):
        self.last_name = l
        
    def change_date_of_birth(self, d):
        self.date_of_birth = d
        
    def update_grade_level(self):
        self.grade_level = self.grade_level + 1
        
StudentID1 = StudentID("2026-45210", "Juan", "Dela Cruz", "10/23/07", 8)
StudentID2 = StudentID("3125-12141", "Pedro", "Garcia", "02/14/05", 5)

print("Number before:", StudentID1.number)
StudentID1.change_number("3125-12141")
print("Number after:", StudentID1.number)

print("First_name before:", StudentID1.first_name)
StudentID1.change_first_name("Pedro")
print("First_name after:", StudentID1.first_name)

print("Last_name before:", StudentID1.last_name)
StudentID1.change_last_name("Garcia")
print("Last_name after:", StudentID1.last_name)

print("Date_of_birth before:", StudentID1.date_of_birth)
StudentID1.change_date_of_birth("02/14/05")
print("Date_of_birth after:", StudentID1.date_of_birth)

print("Before update_grade_level:", StudentID1.grade_level)
StudentID1.update_grade_level()
print("After update_grade_level:", StudentID1.grade_level)

#This is the Laptop class

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

#This is the Dictionary Class

class Dictionary:
    
    def __init__(self, sw, gl, uv, gtp, aw):
        self.search_word = sw
        self.get_language = gl
        self.update_version = uv
        self.go_to_page = gtp
        self.add_word = aw

#Made a set of words with definition so its easier to have something to search
    def __init__(self):
        self.words = {
            "apple": "a fruit that grows on trees and has a red or green skin",
            "banana": "a long curved fruit with a yellow skin",
            "orange": "a round citrus fruit with a thick skin and juicy flesh"
        }
        self.version = 1.0

    def search(self, word):
       
        meaning = self.words.get(word)
        if meaning:
            print(f"The meaning of '{word}' is: {meaning}")
        else:
            print(f"'{word}' not found in the dictionary.")

    def get_language(self, word):
        print(f"The language of '{word}' is English.")

    def update_version(self):
        self.version = self.version + 1.0 
        print(f"Updated dictionary version to {self.version}.")

    def go_to_page_number(self, page_number):
        print(f"Going to page {page_number} in the dictionary...")

    def add_new_word(self, word, meaning):
        print(f"Adding '{word}': {meaning} to the dictionary...")

#Example usage:
dictionary = Dictionary()

dictionary.search("apple")
dictionary.get_language("apple")
dictionary.update_version()
dictionary.go_to_page_number(42)
dictionary.add_new_word("orange", "a round citrus fruit")

# This is the Garden class
class Garden:
	def __init__(self, so, se, wa, su, fl):
		self.soil = so
		self.seed = se
		self.water = wa
		self.sunlight = su
		self.flower = fl
		

	def changesoiltype(self,so):
	    self.soil = so
	def changewatertemp(self,wa):
	    self.water = wa
	def sunstatus(self):
	    return self.sunlight
	def getseedname(self):
	    return self.seed
	

garden1 = Garden("black", "tomato", "cold", "on", "no")
garden2 = Garden("brown", "potato", "warm", "off", "yes")


print("Soil used for plant 1:",garden1.soil)
garden1.changesoiltype(garden2.soil)
print("Soil used for plant 2:", garden1.soil)

print("Water temperature needed for plant 1:", garden1.water)
garden1.changewatertemp("warm")
print("Water used for plant 1:", garden1.water)

print("Sunlight available for plant 1:", garden1.sunlight)

print ("Will flower 1 grow?",garden1.flower)

print("Sunlight status for plant 2:",garden2.sunstatus())

print("Seed used for plant 1:",garden1.getseedname())
print("Seed used for plant 2:",garden2.getseedname())

# This is the Coffee class
class Coffee:
	def __init__(self, p, w, c, m, t, s):
		self.powder = p
		self.water = w
		self.cream = c
		self.mug = m
		self.teaspoon = t
		self.waterstatus = s
		
	def heatwater(self, s):
		self.waterstatus = s
	def getcoffeename(self):
	    self.powder
	def getmugsize(self):
	    self.mug
	def changewater(self, w):
	    self.water = w
	def usespoon(self):
	    self.teaspoon

coffee1 = Coffee("arabica", "distilled", "fullcream", "large", "silver", "cold")
coffee2 = Coffee("robusta", "alkaline", "lowfat", "medium", "wooden", "hot")
print("waterstatusbefore:", coffee1.waterstatus)
coffee1.heatwater("hot")
print("waterstatusafter:", coffee1.waterstatus)
coffee1.getcoffeename()
print("Coffee powder 1:",coffee1.powder)
coffee2.getmugsize()
print("Mug size for coffee 2:",coffee2.mug)
print("Water type before:", coffee2.water)
coffee2.changewater("distilled")
print("Water type after:", coffee2.water)
print("Teaspoon type used for coffee 1:", coffee1.teaspoon)
