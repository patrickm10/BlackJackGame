"""
Class for a deck object
"""

from card import Card
import random

class Deck:
    def __init__(self):
        self.deck = []
        self.build()

    def build(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        for suit in suits:
            for value in values:
                self.deck.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.deck)

    def draw_card(self):
        return self.deck.pop(0)

    def __str__(self):
        return f"Deck: {self.deck}"

    def __repr__(self):
        return f"Deck: {self.deck}"

    def get_deck(self):
        return self.deck

    def get_size(self):
        return len(self.deck)

    def clear_deck(self):
        self.deck.clear()

    def build_deck(self):
        self.build()

    def shuffle_deck(self):
        self.shuffle()

    def get_deck_size(self):
        return self.get_size()

    def get_deck(self):
        return self.get_deck()


# Test the Deck class

# Create a deck
deck = Deck()


# Shuffle the deck
deck.shuffle()
print(f'{deck}\n')

# Draw a card
card = deck.draw_card()
print(f'Drawn card: {card}\n')
print()

# Get the size of the deck
print(deck.get_size())
