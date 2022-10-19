
from Impl.UserServiceImpl import UserServiceImpl

#------------- Product Controller ------------
#El proposito de los controladores es la respuesta que se le da al usuario a la interaccion que hace en la interfaz
#este realiza las peticiones al modelo para pasar estos a la vista. Basicamente lo que se busca con el controlador,
#es de cierta forma monitorear y responder a las peticiones que realiza el usuario a la interfaz. 

#De esta forma este controlador manejara las respuestas del agregar usuario, eliminarlo y actualizarlo.

class UserController():

    UserService: UserServiceImpl

    def __init__(self):
        self.userService = UserServiceImpl()

class Create(UserController):
    def create_user(self):
        self.userService.add_User()

class Update(UserController):
    def update_user(self):
        self.userService.update_User()

class delete(UserController):  
    def delete_user(self):
        self.userService.delete_User()