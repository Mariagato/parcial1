from Factories.ProductFactory import ProductFactory
from Factories.UserFactory import UserFactory
from Impl.WholesaleUser import WholesaleUser

#Este factory se implemento con el fin de darle gestion a los tipos de usuario que existen, para asi complementar el user factory y darle paso a un abstract factory

class WholesaleUserFactory(UserFactory):
    def add_Users(user_Type):
        return WholesaleUser()

    