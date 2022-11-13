import urllib.request, json

class AccuWeatherService():
    _apikey = "09AvZ5ird00p5VVrso4VE5mBSsa8GyuR"
    #_apikey = "2345678"
    _search_url = "http://dataservice.accuweather.com/locations/v1/cities/search"
    _forecast_url = "http://dataservice.accuweather.com/forecasts/v1/daily/1day/"

    @classmethod
    def get_location_key_by_city(cls, search_args):
        req_url = "{}?apikey={}&q={}".format(AccuWeatherService._search_url, AccuWeatherService._apikey, search_args)
        try:
            response = urllib.request.urlopen(req_url)
            data = response.read()
            res_data = json.loads(data)
            return cls.get_forecast_by_location_key(res_data[0]["Key"])
        except Exception as error:
            return False, error
        
    @classmethod
    def get_forecast_by_location_key(cls, location_key):
        req_url = "{}{}?apikey={}".format(AccuWeatherService._forecast_url, location_key, AccuWeatherService._apikey)
        try:
            response = urllib.request.urlopen(req_url)
            data = response.read()
            res_data = json.loads(data)
            return True, res_data["DailyForecasts"]
        except Exception as error:
            return False, error