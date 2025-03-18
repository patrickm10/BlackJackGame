"""
Class for a dealer object
"""

from hand import Hand
from card import Card

class Dealer:
    def __init__(self):
        self.hand = Hand()

    def __str__(self):
        return f"Dealer's hand: {self.hand}"

    def __repr__(self):
        return f"Dealer's hand: {self.hand}"

    def get_hand(self):
        return self.hand

    def add_card(self, card):
        self.hand.add_card(card)

    def clear_hand(self):
        self.hand.clear_hand()

    def get_hand_value(self):     
        return self.hand.get_value()

    def get_hand_size(self):
        return self.hand.get_size()

    def get_hand_status(self):
        return self.hand.get_status()


# Test the dealer class

# Create a dealer
dealer = Dealer()
print(dealer)

# Add a card to the dealer's hand
dealer.add_card(Card('Hearts', 'A'))
print(dealer)

# Clear the dealer's hand
dealer.clear_hand()
