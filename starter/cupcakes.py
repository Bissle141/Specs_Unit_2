from abc import ABC, abstractmethod

class Cupcake(ABC):
    size = 'regular'
    
    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []
  
    def add_sprinkles(self, *args):
        ''' adds passed sprinkes to the instances sprinkels attribute'''
        for sprinkle in args:
            self.sprinkles.append(sprinkle)
   
    @abstractmethod
    def calculate_price(self, quantity):
        ''' Will calculate the price of the selected cupcakes'''
        return quantity * self.price
    
    
class Large(Cupcake):
    size = 'large'
    
    def __init__(self, name, price, flavor, frosting,filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []
        
    def calculate_price(self, quantity):
        ''' Will calculate the price of the selected cupcakes'''
        return quantity * self.price
    
    
class Regular(Cupcake):
    size = 'regular'
    
    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []
        
    def calculate_price(self, quantity):
        ''' Will calculate the price of the selected cupcakes'''
        return quantity * self.price
    
    
class Mini(Cupcake):
    size = 'mini'
    
    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []
        
    def calculate_price(self, quantity):
        ''' Will calculate the price of the selected cupcakes'''
        return quantity * self.price
        
        
my_cupcake_mini = Mini("Chocolate", 1.99, "Chocolate", "White")
# print(my_cupcake_mini.name)
# print(my_cupcake_mini.price)
# print(my_cupcake_mini.size)
# my_cupcake_mini.add_sprinkles('chocolate','rainbow')
# print(my_cupcake_mini.sprinkles)
# print(my_cupcake_mini.calculate_price(13))
my_cupcake = Regular("Cookies and Cream", 2.99, "Chocolate", "Oreo", "Vanilla")
my_cupcake.add_sprinkles('Oreo crumbs')
print(my_cupcake.size,my_cupcake.name,my_cupcake.price,my_cupcake.flavor,my_cupcake.frosting,my_cupcake.filling, my_cupcake.sprinkles)
