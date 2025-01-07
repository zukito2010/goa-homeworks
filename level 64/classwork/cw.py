# instance methods - best for operations on instances of the class (objects)
# static methods - best for utility functions that do not need to access class data
# class methods - best for class level data or require access of class itself

# 1) differences between instance methods and class methods: instance methods does not need a decorators, instance method is used on objects while class method on class itself,  instance`s parameter is self  while class`s is cls
#
# 2) differences between instance methods and static methods: static methods need a decorator; static method does`nt has access to the object attributes or the class attributes; static method is used for independent functions  and does not need parameter.
# 
# 3) differences between class methods and static methods: class has cls argument and static has none; class methods can access class attributes; 

# 4) we use instance method if the logic defines the state of the object;When a method needs to access the attributes of a class but not the attributes of a specific object is when we use class method. When a function logically belongs to a class, but does not require self (object) or cls (class) (static method).

# 5)

class Food:
    food_count = 0
    
    def __init__(self,name,origin,rating):
        self.name = name
        self.origin = origin
        self.rating = rating
        Food.food_count += 1
    
    @classmethod
    def count_food(cls):
        return cls.food_count
    
    @staticmethod
    def shoul_eat(rating):
        if rating > 6:
            return 'you should eat it'
        else :
            return 'you should`nt eat it'
    
    def print_info(self):
        print(f"Food Name: {self.name}, Origin: {self.origin}, Rating: {self.rating}")


    
    
    
 