import random

class Pile:
    def __init__(self, data=None):
        self.cards = data or []

    def shuffle(self):
        random.shuffle(self.cards)

    def top(self):
        return self.cards[-1]

    def put_top_card_on_bottom(self):
        top = self.cards[-1]
        for i in range(len(self.cards) - 1, 0, -1):
            self.cards[i] = self.cards[i - 1]
        self.cards[0] = top

    def add_cards(self, card_list, index=None):
        if index is None:
            self.cards.extend(card_list)
        else:
            self.cards = self.cards[:index] + card_list + self.cards[index:]

    def draw(self, n):
        if n > len(self.cards):
            raise ValueError('Too few cards to draw')

        result = self.cards[-n:]
        self.cards = self.cards[:-n]
        return result

    def __getitem__(self, ix):
        return self.cards[ix]

    def __iter__(self):
        for card in self.cards:
            yield card

    def pop(self, ix):
        return self.cards.pop(ix)

    def __len__(self):
        return len(self.cards)