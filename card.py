"""
Class for a card object
"""

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def __repr__(self):
        return f"{self.value} of {self.suit}"

    def get_value(self):
        if self.value in ['J', 'Q', 'K']:
            return 10
        elif self.value == 'A':
            return 11
        else:
            return int(self.value)

    def get_suit(self):
        return self.suit

    def get_face(self):
        return self.value

    def get_card(self):
        return self


# Test the card class

# Create a card
card = Card('Hearts', 'A')
print(card)
print(card.get_value())

