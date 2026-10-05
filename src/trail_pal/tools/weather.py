import requests
from dotenv import load_dotenv
import os

from trail_pal.tools.memoryAgent import MemoryAgent

class WeatherAgent:
    def __init__(self, api_key:str, memory: MemoryAgent):
        self.api_key = api_key
        self.memory = memory
        self.url = "http://api.openweathermap.org/data/2.5/weather"

    def answer(self, city:str):
        params = {
            "city": city,
            "appid": self.api_key,
            "units": "metrics" 
        }

        res = requests.get(self.url, params=params)

        if res!=200:
            return "I couldn't retrieve the weather right now."

        data = res.json()

        previous = self.memory.recall(city)
        self.memory.store(city, data["main"])

        response = (
                    f"The current weather in {city} is {data['weather'][0]['description']} "
                    f"with a temperature of {data['main']['temp']}°C."
                )

        if previous:
            response += f" Earlier it was {previous['temp']}°C."

        return response


if __name__ == "__main__":
    load_dotenv()
    memoryAgent = MemoryAgent()
    weather = WeatherAgent(os.getenv("OPEN_WEATHER"), memoryAgent)
    print(weather.answer("Berlin"))
