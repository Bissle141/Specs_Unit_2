from abc import ABC, abstractmethod
import csv
from pprint import pprint

cupcake_menu = 'sample.csv'

class Cupcake(ABC):
    def __init__(self, size, name, price, flavor, frosting, filling):
        self.size = size
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
    
    def __init__(self, name, price, flavor, frosting, filling="none"):
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
        
        
# my_cupcake_mini = Mini("Chocolate", 1.99, "Chocolate", "White")
# my_cupcake = Regular("Cookies and Cream", 2.99, "Chocolate", "Oreo", "Vanilla")
# my_cupcake.add_sprinkles('Oreo crumbs')


# cupcakes_list = [my_cupcake,my_cupcake_mini]


# def read_csv_file(csv_file):
#     with open(csv_file) as file:
#         lines = csv.DictReader(file)

#         for row in lines:
#             pprint(row)
            
# def write_new_csv(file, cupcakes):
#     with open(file, "w", newline="\n") as csvfile:
#         fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
#         writer.writeheader()
        
#         for cupcake in cupcakes:
#             if hasattr(cupcake, "filling"):
#                 writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles, "filling": cupcake.filling})
            
#             else:
#                 writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})
                
# def add_cupcake(file, cupcake):
#     with open(file, "a", newline="\n") as csvfile:
#         fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#         if hasattr(cupcake, "filling"):
#             writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
#         else:
#             writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})
    
def write_list_to_csv(file, list):
    with open(file, "w", newline='\n') as order_file:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling", "quantity"]
        writer = csv.DictWriter(order_file, fieldnames=fieldnames)
        
        writer.writeheader()
        
        writer.writerows(list)  
    
def get_cupcakes(file):
    with open(file) as cupcakefile:
        reader = csv.DictReader(cupcakefile)
        reader = list(reader)
        return reader
    
def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
    return None    

def add_cupcake_dictionary(file, cupcake):
    order_list = get_cupcakes(file)
    name = cupcake['name']
    exists = False
    
    for item in order_list:
        if item['name'] == name:
            item['quantity'] = 1 + int(item['quantity'])
            exists = True
            break
    if not exists: 
        cupcake['quantity'] = 1
        order_list.append(cupcake)
    
    write_list_to_csv(file, order_list)     
        
def get_total(file):
    total = 0.00
    for cupcake in get_cupcakes(file):
        total += (float(cupcake["price"]) *  float(cupcake["quantity"]))
        
    return round(total,2)

def del_cupcake(file, name):
    order_list = get_cupcakes(file)
    
    for item in order_list:
        if item['name'] == name:
            order_list.remove(item)
            break
    
    write_list_to_csv(file, order_list)

def add_to_quan(file, name):
    order_list = get_cupcakes(file)
    
    for item in order_list:
        if item['name'] == name:
            item['quantity'] = 1 + int(item['quantity'])
            break
        
    write_list_to_csv(file, order_list)

def minus_from_quan(file, name):
    order_list = get_cupcakes(file)
    
    for item in order_list:
        if item['name'] == name:
            if int(item['quantity']) == 1:
                order_list.remove(item)
                break
            else:
                item['quantity'] = int(item['quantity']) - 1
                break
    
    write_list_to_csv(file, order_list)