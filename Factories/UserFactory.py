from abc import ABC, ABCMeta, abstractmethod, abstractstaticmethod
from Impl.OccasionalUser import OccasionalUser

from Impl.WholesaleUser import WholesaleUser
#Aqui se busco implementar un abstract factory para las variaciones que tiene el usuario, tipo de usuario
#El patrón Abstract Factory: es útil cuando el cliente desea crear una instancia de una familia de clases dependientes relacionadas sin tener que saber qué clase concreta específica se debe instanciar.
class UserFactory(ABC):
    @abstractmethod
    def add_Users(user_Type):
        pass


