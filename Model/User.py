from Services.UserType import UserType
class User:

#Lo unico diferente que encontramosn en este modelo es la instancia de la clase userType, esto con el
#proposito de que salude al usuario dependiendo del tipo de usuario que sea.

    user : UserType

    def __init__(self, name, identification, address, phoneNumber, email, userType):
        self.name = name
        self.identification = identification
        self.address = address
        self.phoneNumber = phoneNumber
        self.email = email
        self.userType = userType

    def hello(self):
        print("HIII")
        self.userType.hello()
