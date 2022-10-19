
from abc import ABC, abstractmethod


class ProductService(ABC):

    @abstractmethod
    def add_Product(self, name, sku, description, price, material, color, available_stock, creation_date ):
        pass

    @abstractmethod
    def search_Product(self, sku):
        pass

    @abstractmethod
    def update_Product(self, name, description, price, update_date ):
        pass

    @abstractmethod
    def delete_Product(self, sku):
        pass