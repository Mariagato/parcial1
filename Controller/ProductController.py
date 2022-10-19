from Impl.ProductServiceImpl import ProductServiceImpl

#------------- Product Controller ------------
#El proposito de los controladores es la respuesta que se le da al usuario a la interaccion que hace en la interfaz
#este realiza las peticiones al modelo para pasar estos a la vista. Basicamente lo que se busca con el controlador,
#es de cierta forma monitorear y responder a las peticiones que realiza el usuario a la interfaz. 

#De esta forma este controlador manejara las respuestas del agregar producto, eliminarlo, actualizarlo y buscarlo.

class ProductController():
    productService : ProductServiceImpl

    def __init__(self):
        self.productService = ProductServiceImpl()

class Create(ProductController):
    def create_product(self):
        self.productService.add_Product()

class update(ProductController):
    def update_product(self):
        self.productService.update_Product()

class delete(ProductController):   
    def delete_product(self):
        self.productService.delete_Product()

class search(ProductController):
    def search_product(self):
        self.productService.search_Product()