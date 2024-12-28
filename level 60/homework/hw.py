class Motorcycle:
    total_motorcycles = 0

    def __init__(self, brand, model, engine_capacity, color):
        self.brand = brand
        self.model = model
        self.engine_capacity = engine_capacity
        self.color = color
        
        Motorcycle.total_motorcycles += 1

    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Engine Capacity: {self.engine_capacity}cc, Color: {self.color}"

# Example usage
bike1 = Motorcycle("BMW", "S 1000 RR", 312, "Green")
bike2 = Motorcycle("Honda", "CBR500R", 222, "Red")

print(bike1.display_info()) 
print(bike2.display_info())
print(Motorcycle.total_motorcycles) 