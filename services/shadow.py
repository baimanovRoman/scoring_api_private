from services.singleton import Singleton
from model.base_model import Item

class Shadow(Singleton):

    def get_data(self, item: Item, result):
        if item.vin in self.dict_data:
            return self.dict_data.get(item.vin)
        self.dict_data[item.vin] = result
        return self.dict_data.get(item.vin)