CARD_REGISTRY = {}

def register_card(card_id):
    def add_subclass_to_registry(subclass):
        CARD_REGISTRY[card_id] = subclass
        setattr(subclass, 'card_id', card_id)
        return subclass
    return add_subclass_to_registry