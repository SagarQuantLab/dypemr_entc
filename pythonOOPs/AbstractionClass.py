from abc import ABC, abstractmethod
class government(ABC):
    def __init__(self, shop_name_application):
        self.application = shop_name_application

    @abstractmethod
    def get_license(self):
        pass

class foodshop(government):

    def __init__(self, raw_materials, name_of_shop):
        self.raw_materials = raw_materials
        self.shop_name = name_of_shop

    def get_license(self):
        return f"Got license for shop {self.shop_name}"