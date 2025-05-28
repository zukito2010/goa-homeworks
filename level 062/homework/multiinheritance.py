class Internet_users:
    def __init__(self,name,):
        self.name = name

    def browsing(self):
        print(f'{self.name} is browsing')

class Phone_users(Internet_users):
    def scroll(self):
        print(f'{self.name} is scrolling')

class Laptop_users(Internet_users):
    def using_laptop():
        pass

class Pc_users(Internet_users):
    def using_pc():
        pass