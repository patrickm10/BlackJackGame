"""
Author: Patrick Mejia
Date: 3/18/2025
Description: This is the main game file for the BlackJack game with a probability analyzer.
"""

from deck import Deck
from player import Player
from dealer import Dealer
from hand import Hand
from card import Card


class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Patrick")
        self.dealer = Dealer()

    def start_game(self):
        print("Welcome to BlackJack!\n")

        # Build the deck
        self.deck.build_deck()
        self.deck.shuffle_deck()

        # Deal the cards
        self.deal_cards()

        # Display the cards
        self.display_cards()

        # Player's turn
        self.player_turn()

        # Dealer's turn
        self.dealer_turn()

        # Determine the winner
        self.determine_winner()

    def deal_cards(self):
        # Deal one card to the player
        self.player.add_card(self.deck.draw_card())

        # Deal two cards to the dealer
        self.dealer.add_card(self.deck.draw_card())
        self.dealer.add_card(self.deck.draw_card())
        self.dealer.hide_second_card()

    def display_cards(self):
        print(f"Player's hand: {self.player.get_hand()} --- Value: {self.player.get_hand_value()}")
        print(f"Dealer's visible card: {self.dealer.get_visible_card()}")

    def player_turn(self):
        while self.player.get_hand_value() < 21:
            self.calculate_win_probability()
            choice = input("Do you want to hit or stand? (h/s): ")
            if choice == "h":
                self.player.add_card(self.deck.draw_card())
                print(f"Player's hand: {self.player.get_hand()} --- Value: {self.player.get_hand_value()}")
                if self.player.get_hand_value() > 21:
                    print("Player busts!")
                    break
            else:
                self.dealer.reveal_second_card()
                print(f"Dealer's hand: {self.dealer.get_hand()} --- Value: {self.dealer.get_hand_value()}")
                break

    def dealer_turn(self):
        while self.dealer.get_hand_value() < 17:
            self.dealer.add_card(self.deck.draw_card())
            print(f"Dealer's hand: {self.dealer.get_hand()} --- Value: {self.dealer.get_hand_value()}")
            if self.dealer.get_hand_value() > 21:
                print("Dealer busts!")
                break

    def determine_winner(self):
        player_value = self.player.get_hand_value()
        dealer_value = self.dealer.get_hand_value()

        print(f"Player's hand value: {player_value}")
        print(f"Dealer's hand value: {dealer_value}")

        if player_value > 21:
            print("Dealer wins!")
        elif dealer_value > 21:
            print("Player wins!")
        elif player_value == dealer_value:
            print("It's a push!")
        elif player_value > dealer_value:
            print("Player wins!")
        else:
            print("Dealer wins!")

        print("\nGame over!")
        self.player.clear_hand()
        self.dealer.clear_hand()

    def calculate_win_probability(self):
        """Estimate the probability of winning based on the dealer's visible card and remaining deck."""
        player_value = self.player.get_hand_value()
        
        dealer_visible_card = self.dealer.get_visible_card()  # Get the visible Card object
        if isinstance(dealer_visible_card, Card):
            dealer_visible = dealer_visible_card.get_value()  # Ensure we get an integer value
        else:
            print("Error: Dealer's visible card is invalid.")
            return
        
        remaining_cards = self.deck.get_remaining_cards()

        if not isinstance(dealer_visible, int):
            print(f"Error: Dealer's visible card value is not an integer: {dealer_visible}")
            return

        # Calculate the probability of winning
        if 2 <= dealer_visible <= 6:
            bust_prob = sum(1 for card in remaining_cards if card.get_value() > 6)
            win_prob = (bust_prob / len(remaining_cards)) * 100 if remaining_cards else 0
            print(f"Win probability: {win_prob:.2f}%")
        elif 7 <= dealer_visible <= 11:
            high_hand_prob = sum(1 for card in remaining_cards if card.get_value() <= 6)
            win_prob = (high_hand_prob / len(remaining_cards)) * 100 if remaining_cards else 0
            print(f"Win probability: {win_prob:.2f}%")
        else:
            print("Win probability: 0.00%")


# Test the game
game = Game()
game.start_game()
