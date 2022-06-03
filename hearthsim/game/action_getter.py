class ActionGetter:
    pass

class InputActionGetter(ActionGetter):
    def get_action(self):
        return input().strip()

class TextActionGetter(ActionGetter):
    def __init__(self, text):
        self._lines = text.split('\n')
        self._i = 0

    def get_action(self):
        result = self._lines[self._i].strip()
        self._i += 1
        return result
