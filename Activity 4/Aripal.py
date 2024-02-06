class Car:
    def __init__(self, color, model, manufacturer):
        self.color = color
        self.model = model
        self.manufacturer = manufacturer

# Instantiate the Car class three times
car1 = Car("White", "Range Rover", "Jaguar Land Rover")
car2 = Car("BLack", "SUV", "Ford")
car3 = Car("Silver", "McLaren F1", "McLaren Cars")

# Display properties of Range Rover 
print("Car 1:")
print("Color:", car1.color)
print("Model:", car1.model)
print("Manufacturer:", car1.manufacturer)
print()

# Display properties of SUV
print("Car 2:")
print("Color:", car2.color)
print("Model:", car2.model)
print("Manufacturer:", car2.manufacturer)
print()

# Display properties of McLaren
print("Car 3:")
print("Color:", car3.color)
print("Model:", car3.model)
print("Manufacturer:", car3.manufacturer)
print()

# Modify properties of Car 1
car1.color = "Red"
car1.model = "Ferrari 308 GTB/GTS"
car1.manufacturer = "Ferrari"

# Display modified properties of Car 1
print("Modified Car 1:")
print("Color:", car1.color)
print("Model:", car1.model)
print("Manufacturer:", car1.manufacturer)
