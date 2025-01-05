class Bus:
    def __init__(self, m = []) -> None:
        self.m = m

    def pick(self, name):
        self.m.append(name)

    def drop(self, name):
        self.m.remove(name)