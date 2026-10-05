class MemoryAgent:

    def __init__(self):
        self.storage = {}

    def store(self, key:str, value:str)->None:
        self.storage[key] = value

    def recall(self, key:str)->str | object:
        if key:
            return self.storage[key]
        return self.storage
    