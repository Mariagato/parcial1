from enum import Enum

from ProductType import ProductType

#La categoria de un product fue tomada como un enum.


class Product:

    product: ProductType
    

    def __init__(self, name, sku, description, price, material, color, available_stock, creation_date, update_date, productType):
        self.name = name
        self.sku = sku
        self.description = description
        self.price = price
        self.material = material
        self.color = color
        self.available_stock = available_stock
        self.creation_date = creation_date
        self.update_date = update_date
        self.productType = ProductType
        
    def product_method(self):
        print("I am a product")
        self.productType.product_method()

    