"""
Class for a hand object
"""

from card import Card

class Hand:
    def __init__(self):
        self.hand = []
        self.status = "In Play"
        self.value = 0
        self.size = 0

    def __str__(self):
        return ", ".join([str(card) for card in self.hand])

    def __repr__(self):
        return ", ".join([str(card) for card in self.hand])

    def add_card(self, card):
        self.hand.append(card)
        self.size += 1
        self.value += card.get_value()
        if self.value > 21:
            self.status = "Bust"

    def clear_hand(self):
        self.hand = []
        self.status = "In Play"
        self.value = 0
        self.size = 0

    def get_value(self):
        return self.value

    def get_size(self):
        return self.size

    def get_status(self):
        return self.status

    def get_hand(self):
        return self.hand

    def get_hand_value(self):
        return self.value


# Test the hand class

# Create a hand
hand = Hand()
print(hand)

# Add a card to the hand
hand.add_card(Card('Hearts', 'A'))
print(hand)
print(hand.get_value())
