import requests
from dotenv import load_dotenv
import os

from trail_pal.tools.memoryAgent import MemoryAgent

class WeatherAgent:
    def __init__(self, memory: MemoryAgent):
        self.memory = memory
        self.url = "http://api.openweathermap.org/data/2.5/weather"

        load_dotenv()
        self.api_key = os.getenv("OPEN_WEATHER")


    def answer(self, city:str="Nuwara Eliya"):
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric" 
        }

        res = requests.get(self.url, params=params, timeout=10)

        if res.status_code!=200:
            return "I couldn't retrieve the weather right now."

        data = res.json()

        previous = self.memory.recall("weather")
        self.memory.store_weather(data["main"])

        response = (
                    f"The current weather in {city} is {data['weather'][0]['description']} "
                    f"with a temperature of {data['main']['temp']}°C."
                )

        if previous!=None:
            response += f" Earlier it was {previous}°C in this conversation."

        final_res = {"role": "system", "content": response}
        return final_res
