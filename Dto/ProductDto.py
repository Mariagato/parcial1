#----------------- DTO ---------------
# Un dto es un Data Transfer Object, son un tipo de datos que sirven unicamente
# para transportar datos. El Dto contiene ciertas propiedades del objeto. En este caso 
#le di paso a un dto debido a lo que se mencionaba en el texto respecto a las variaciones. 
#Basicamente con un dto lo que se logra es que el metodo update sea con atributos especificos y no
#se tenga que actualizar cada uno de los atributos del objeto para poder hacer un update.


class ProductDto:
    def __init__(self, name, price, description, material, color, available_Stock) -> None:
        self.name = name
        self.price = price
        self.material = material
        self.color = color
        self.available_stock = available_Stock
        self.description = description