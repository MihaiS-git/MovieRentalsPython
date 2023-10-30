class InMemoryRepository:
    def __init__(self):
        self.data = {}

    def create(self, key, value):
        if key in self.data:
            raise KeyError("Key already exists")
        self.data[key] = value

    def read(self, key):
        if key in self.data:
            return self.data[key]
        else:
            raise KeyError("Key not found")

    def update(self, key, value):
        if key in self.data:
            self.data[key] = value
        else:
            raise KeyError("Key not found")

    def delete(self, key):
        if key in self.data:
            del self.data[key]
        else:
            raise KeyError("Key not found")

    