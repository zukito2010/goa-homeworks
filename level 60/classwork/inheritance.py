# with inheritance
class Animal:
    def __init__(self, name,color):
        self.name = name
        self.color = color

    def move(self):
        print(f'{self.name} is moving')
class Dog(Animal):
    def bark(self):
        print('woof')
class cat(Animal):
    def meow(self):
        print('meow')

maxx = Dog('Max', 'black')

maxx.bark()
maxx.move()