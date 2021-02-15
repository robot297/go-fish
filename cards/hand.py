"""Holds information all the player's hand"""


class Hand:
    """All information on the players hand"""

    def __init__(self):
        """Constructor for player hands"""
        self.cards = []
        self.books = []

    def check_if_in_hand(self, card):
        """Returns True if card is in hand, False if not"""
        if card not in self.cards:
            return False
        else:
            return True

    def draw_card(self, card_selected, to_hand):
        """Draws card from one hand and places it into another."""
        x = 0
        card_selected = card_selected.upper()
        while card_selected in self.cards:
            to_hand.append(card_selected)
            self.cards.remove(card_selected)
            x = x + 1
        print(f'{x} card(s) were drawn.')
        return to_hand

    def book_check(self, picked_card):
        picked_card = picked_card.upper()
        if self.cards.count(picked_card) == 4:
            self.books.append(picked_card)

            for x in range(4):
                self.cards.remove(picked_card)
            print(f'A book made of {picked_card}\'s has been made')

    def __str__(self):
        """Returns the players cards"""
        return str(self.cards)
