#Metodo abstracto del mensaje de aqui heredan 

from abc import ABCMeta, abstractstaticmethod

#Aquí implementamos el metodo que compartiran los usuarios, en este caso hello, que es un saludo dependiendo del tipo de usuario que sea
class ProductType(meta=ABCMeta):
    @abstractstaticmethod
    def User_method():
        """Interface Method"""