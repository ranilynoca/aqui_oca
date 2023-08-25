# This is the StudentID class
class StudentID:
    def __init__(self, n, f, l, d, g):
        self.__number = n  # This is the private attribute
        self.first_name = f
        self.last_name = l
        self.date_of_birth = d
        self.grade_level = g
        
    def change_number(self, n):
        self.__number = n
        
    def change_first_name(self, f):
        self.first_name = f
        
    def change_last_name(self, l):
        self.last_name = l
        
    def change_date_of_birth(self, d):
        self.date_of_birth = d
        
    def update_grade_level(self):
        self.grade_level += 1  
        
    def get_number(self):
        return self.__number  
        

# This CollegeStudent class inherits from the StudentID class
class CollegeStudent(StudentID):
    def __init__(self, n, f, l, d, g, major):
        super().__init__(n, f, l, d, g)  
        self.major = major
        
    def change_major(self, new_major):
        self.major = new_major
        


StudentID1 = StudentID("2026-45210", "Juan", "Dela Cruz", "10/23/07", 8)
CollegeStudent1 = CollegeStudent("3125-12141", "Pedro", "Garcia", "02/14/05", 5, "Computer Science")


print("Number before:", StudentID1.get_number())  # Using the getter method
StudentID1.change_number("3125-12141")
print("Number after:", StudentID1.get_number())

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

print("Major:", CollegeStudent1.major)
CollegeStudent1.change_major("Electrical Engineering")
print("New Major:", CollegeStudent1.major)

# This is the Coffee class
class Coffee:
	def __init__(self, p, w, c, m, t, s):
		self.powder = p
		self.water = w
		self.cream = c
		self.__mug = m  # private attribute
		self.teaspoon = t
		self.waterstatus = s
		
	def heatwater(self, s):
		self.waterstatus = s
	def getcoffeename(self):
	    self.powder
	
	def changewater(self, w):
	    self.water = w
	def usespoon(self):
	    self.teaspoon
	def set_mugsize(self,m):#setter method - private attribute
	    self.__mug = m
	def get_mugsize(self): #getter method - private attribute
	    print(self.__mug)
	    self.__get_mugsize() #referencing private method within parent class
	
	def __get_mugsize(self): #private method for parent class
	    print(self.__mug)
	
class Cappuccino(Coffee): #child class of Coffee class
    def __init__(self, sg, p, w, c, m, t, s):
        super().__init__(p, w, c, m, t, s) 
        self.sweetener = sg #unique attribute to this class
    
    def add_sweetener(self): #unique method to this class
        print("Sugar used:",self.sweetener)

#objects for parent class    
coffee1 = Coffee("arabica", "distilled", "fullcream", "large", "silver", "cold")
coffee2 = Coffee("robusta", "alkaline", "lowfat", "medium", "wooden", "hot")

#referencing public methods/attributes of parent class
print("waterstatusbefore:", coffee1.waterstatus)
coffee1.heatwater("hot")
print("waterstatusafter:", coffee1.waterstatus)
coffee1.getcoffeename()
print("Coffee powder 1:",coffee1.powder)

#referencing private attribute of parent class through getter and setter methods
coffee2.set_mugsize("extra large")
print("Mug size for coffee 2:")
coffee2.get_mugsize()

#referencing public methods/attributes of parent class
print("Water type before:", coffee2.water)
coffee2.changewater("distilled")
print("Water type after:", coffee2.water)
print("Teaspoon type used for coffee 1:", coffee1.teaspoon)

#object for child class
cappuccino1 = Cappuccino("brown", "peruvian","sparkling","highfat","small","plastic","veryhot")
#referencing method of child class
cappuccino1.add_sweetener()
