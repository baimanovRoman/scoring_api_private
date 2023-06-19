import pandas as pd
import os
from random import randrange
from model.base_model import Item
from datetime import datetime
from services.shadow import Shadow

class GetData:
    def __init__(self, item: Item):
        self.path_to_file = '{path}/data/id02_06042023_enq_resp_wo_pd.csv'.format(path=os.getcwd())
        self.item = item
        self.format_datetime = "%d.%m.%Y"
        self.random_id = randrange(269352)

    def __call__(self, *args, **kwargs):
        dataframe = pd.read_csv(self.path_to_file, sep=";", encoding="cp1251")
        result_array = dataframe.astype('object').iloc[self.random_id]
        result_array.fillna('', inplace=True)
        result_array = self.__parser(result_array)
        shadow_class = Shadow()
        result_array = shadow_class.get_data(self.item, result_array)
        return result_array.get('data').to_dict() if result_array.get('flag') else result_array.get('data')

    def __valid(self):
        if len(self.item.vin) != 17:
            return {
                "flag": False,
                "data": {
                    "Exception": "not correct vin"
                }
            }
        try:
            str_datetime = datetime.strptime(self.item.birth_date, self.format_datetime)
        except Exception as e:
            return {
                "flag": False,
                "data": {
                    "Exception": "Date birth day not correct format 'dd.mm.yy'"
                }
            }
        return {"flag": True, "data": {}}
    def __parser(self, result_array):
        data = self.__valid()
        result_array['VIN'] = self.item.vin
        result_array['vin'] = self.item.vin
        result_array['дата рождения'] = self.item.birth_date
        result_array['возраст'] = self.__get_age()
        return {
            "flag": True,
            "data": result_array} if data.get('flag') else data

    def __get_age(self):
        datetime_now = datetime.now()
        datetime_birth_day = datetime.strptime(self.item.birth_date, self.format_datetime)
        year = int(round((datetime_now - datetime_birth_day).days/365,0))
        return year