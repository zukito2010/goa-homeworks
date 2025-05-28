class Car:
    # class variable
    x = 0
    
    def __init__(self, brand,model, color, year): 
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        # instance variables
    
    # __x__ dunder methods
    
    # methods
    def go(self):
        print(f'{self.model} is going')
    
    def stop(self):
        print(f'{self.model} has stopped')

car1 = Car('Ford', 'Mustang','Black', 2005)
car2 = Car(brand='porsche', model='taycan', color='red', year=2023)

print(car1.brand)
print(car1.model)
print(car1.color)
print(car1.year)
print()
print(car2.brand)
print(car2.model)
print(car2.color)
print(car2.year)

car1.go()
car1.stop()
car2.go()
car2.stop()



# dunder methods are methods that starts and ends with the __ for example __init__

# instance variables is variebles for our blue prints atributes

#class variable is a variable inside class block 

# blue print is like scetch (or a drawing) for the project you are making 