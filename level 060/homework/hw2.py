class Children:
    
    def __init__(self,name,age,fav_toy):
        self.name = name
        self.age = age
        self.fav_toy = fav_toy
    
    def play(self):
        print(f'{self.name} is playing with his {self.fav_toy}')
class Teen(Children):
    def look_at_phone(self):
        print(f'{self.name} is watching videos on his phone')
class Almost_adult(Children):
    def getting_license(self):
        print(f'{self.name} is already {self.age} years old so he can get a driving license')


ryan = Children('Ryan',7,'rubic`s cube')
john = Teen('John',13,'toy car') 
gary = Almost_adult('Gary',17,'water gun') 

ryan.play()
john.look_at_phone()
gary.getting_license()