class WeatherAgent:
    def __init__(self, api_key:str):
        self.api_key = api_key
        self.url = "http://api.openweathermap.org/data/2.5/weather"

    def answer(self, city:str):
        params = {
            "city": city,
            "appid": self.api_key,
            "units": "metrics" 
        }

