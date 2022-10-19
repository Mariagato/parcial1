from enum import Enum

#La categoria de un product fue tomada como un enum.

class Category(Enum):
    ELECTRONICACCESSORY = 1
    DECORATIVEACCESSOR = 2
    COMPUTER = 3
    PHONE = 4

class Product:
    

    def __init__(self, name, sku, description, price, material, color, available_stock, creation_date, update_date):
        self.name = name
        self.sku = sku
        self.description = description
        self.price = price
        self.material = material
        self.color = color
        self.available_stock = available_stock
        self.creation_date = creation_date
        self.update_date = update_date
        self.category = Category

    