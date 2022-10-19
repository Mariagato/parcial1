#Metodo abstracto del mensaje de aqui heredan 

from abc import ABC, abstractmethod

#Aquí implementamos el metodo que compartiran los usuarios, en este caso hello, que es un saludo dependiendo del tipo de usuario que sea
class UserType(ABC):
    @abstractmethod
    def hello(self):
        pass