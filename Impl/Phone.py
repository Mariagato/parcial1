from Model.Product import Product
from ProductType import ProductType

#Los tipos de productos pasaron de ser arrays a clases
class Phone(Product):
    def product_method(self):
        print("Im a phone")