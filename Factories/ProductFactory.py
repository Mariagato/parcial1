from Impl.DecorativeAccessory import DecorativeAccessory
from Impl.ElectronicAccesory import ElectronicAccessory
from ..Impl.Computer import Computer
from ..Impl.Phone import Phone

#Esta factory hace uso de el tipo de productos, de esta manera cada tipo de producto realizara el mismo metodo pero separando 
#preocipaciones por medio del factory, lo que se busca con este es la separacion de responsabilidades y preocupaciones como 
#anteriormente lo mencionaba. Este es un factory method. 

class ProductFactory:

    @staticmethod
    def build_product(product_type):
        if product_type == "Computer":
            return Computer()
        if product_type == "Phone":
            return Phone()
        if product_type == "Decorative Accessory":
            return DecorativeAccessory()
        if product_type == "electronic accessory":
            return ElectronicAccessory()
        print("invalid type")
        return -1

if __name__ == "__main__":
    choice = input("What kind of product do you want to create?\n")
    product = ProductFactory.build_product(choice)
    product.product_method

#Para concluir y resumir la responsabilidad de la clase esta maneja la construcción de 
#productos y de sus variaciones, como los distintos tipos que existen