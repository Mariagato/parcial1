#ABC metodo abstracto 

from abc import abstractmethod, ABC


class UserService(ABC):

    @abstractmethod
    def add_User(self,name, identification, address, phoneNumber, email, userType):
        pass

    @abstractmethod
    def update_User(self, name, address, phoneNumber, email):
        pass

    @abstractmethod
    def delete_User(self, identification):
        pass
