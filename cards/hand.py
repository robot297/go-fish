"""Holds information all the player's hand"""
class Hand:
    """All information on the players hand"""

    def __init__(self):
        """Constructor for player hands"""
        self.cards = []

    def check_if_in_hand(self, card):
        """Returns True if card is in hand, False if not"""
        if card not in self.cards:
            return False
        else:
            return True
    
    def __str__(self):
        """Returns the players cards"""
        return str(self.cards)
