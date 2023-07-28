#This is the Clay Class

class Clay:
    def __init__(self, color, weight, drying_time, pliability, texture):
        self.color = color
        self.weight = weight
        self.drying_time = drying_time
        self.pliability = pliability
        self.texture = texture

    def mold_shape(self, shape):
        print(f"Molding the clay into a {shape} shape.")

    def add_color(self, new_color):
        print(f"Adding {new_color} color to the clay.")
        self.color = new_color

    def get_weight(self):
        return self.weight

    def get_texture(self):
        return self.texture

    def start_dry(self):
        print("Starting the drying process.")
        self.drying_time = "2 hrs"

clay1 = Clay(color="Red", weight=500, drying_time="2 hrs", pliability="Soft", texture="Smooth")

print("Color:", clay1.color)
print("Weight:", clay1.get_weight())
