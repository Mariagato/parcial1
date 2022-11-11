from abc import ABCMeta,abstractstaticmethod

class ProductType(meta=ABCMeta):
    @abstractstaticmethod
    def product_method():
        """Interface Method"""