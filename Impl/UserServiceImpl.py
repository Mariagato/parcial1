from UserService import UserService

#Los metodos reciben los parametros que necesita para funcionar.

class UserServiceImpl(UserService):
    
    def __init__(self):
        self.users = []

    def add_User(self, name, identification, address, phoneNumber, email, userType):
        return super().add_User(name, identification, address, phoneNumber, email, userType)

    def update_User(self, name, address, phoneNumber, email):
        pass

    def delete_User(self, identification):
        pass

