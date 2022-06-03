class CharacterSelection:
    _events_received = tuple()

    def get_selected_card_slots(self, game, em_node):
        raise NotImplementedError()

    @property
    def events_received(self):
        return self._events_received