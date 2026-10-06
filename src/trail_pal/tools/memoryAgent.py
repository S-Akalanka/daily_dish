class MemoryAgent:

    def __init__(self):
        self.storage = {}

    def store(self, key:str, value:str)->None:
        self.storage[key] = value

    def recall(self, key:str)->int | object:
        if key in self.storage:
            return self.storage[key]
        return None
    