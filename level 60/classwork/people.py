class Person:
    ppl_count = 0
    
    def __init__(self, name , age , country):
        self.name = name
        self.age = age
        self.country = country
        Person.ppl_count += 1
    
    def greet(self):
        print(f'Hello {self.name}')
    
    def yell_at_him(self):
        print(f'{self.name.upper()}')
        

person1 = Person('Zuka', 14, 'Georgia')
person2 = Person('Yuri', 17, 'Russia')
person3 = Person('George', 15, 'USA')


print(person1.name)
print(person1.age)
print(person1.country)
print(person2.name)
print(person2.age)
print(person2.country)
print(Person.ppl_count)