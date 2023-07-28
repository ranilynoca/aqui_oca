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
