class InMemorySessionService:
    def __init__(self):
        self.store = {}

    def set(self, k, v):
        self.store[k] = v

    def get(self, k, default=None):
        return self.store.get(k, default)
