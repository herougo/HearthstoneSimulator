class Condition:
    _events_received = tuple()

    @property
    def events_received(self):
        return self._events_received

class AndCondition(Condition):
    def __init__(self, condition1, condition2):
        self.condition1 = condition1
        self.condition2 = condition2

    def evaluate(self, game, em_node):
        return self.condition1.evaluate(game, em_node) and self.condition2.evaluate(game, em_node)

    def events_received(self):
        return self.condition1.events_received + self.condition2.events_received

class OrCondition(Condition):
    def __init__(self, condition1, condition2):
        self.condition1 = condition1
        self.condition2 = condition2

    def evaluate(self, game, em_node):
        return self.condition1.evaluate(game, em_node) or self.condition2.evaluate(game, em_node)

    def events_received(self):
        return self.condition1.events_received + self.condition2.events_received