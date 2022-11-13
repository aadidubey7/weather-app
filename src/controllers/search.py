from services.accuweather import AccuWeatherService
from models.search import SearchModel

class SearchController:
    
    def __init__(self, search_args, search_res = []):
        self.search_args = search_args
        self.search_res = search_res

    def store_searched_data(self):
        search_model = SearchModel(self.search_args, self.search_res[0])
        search_model.save()
    
    @classmethod
    def get_location_key_by_city(cls, search_args):
        return AccuWeatherService.get_location_key_by_city(search_args)