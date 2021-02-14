"""Contains all the things you can do for a card deck"""
import random

class Deck:
    """Contains all the things you can do for a card deck"""

    def __init__(self):
        """Builds the deck for the game"""
        self.card_deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K' ] * 4

    def shuffle(self):
        """Shuffles the card deck"""
        random.shuffle(self.card_deck)

    def deal_hand(self):
        """Deals 7 cards to the specified player"""
        dealt_cards = []

        for x in range(7):
            card_dealt = self.card_deck.pop(0)
            dealt_cards.append(card_dealt)
            print(f'{card_dealt} was dealt.')
        
        return dealt_cards

    def __str__(self):
        """Returns the card deck"""
        return str(self.card_deck)
