from ProductService import ProductService

#Los metodos reciben los parametros que necesita para funcionar.

class ProductServiceImpl(ProductService):

    def __init__(self):
        self.products = []

    def add_Product(self, name, sku, description, price, material, color, available_stock, creation_date):
        return super().add_Product(name, sku, description, price, material, color, available_stock, creation_date)

    def update_Product(self, name, description, price, update_date):
        pass

    def delete_Product(self, sku):
        return super().delete_Product(sku)
    
    def search_Product(self, sku):
        pass