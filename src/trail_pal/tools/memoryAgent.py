class MemoryAgent:

    def __init__(self):
        self.storage = {
             "weather":"",
             "history": []
        }

    def store_weather(self, value:str)->None:
        self.storage["weather"] = value

    def store_chat(self, value:str)->None:
            self.storage["history"].append(value)

    def recall(self, key:str)->int | object:
        if key in self.storage:
            return self.storage[key]
        return None
    