"""Unit tests for the Deck class"""
from cards.deck import Deck


def test_deck_0001():
    """Tests if the deck was created properly"""
    test_deck = Deck()
    assert len(test_deck.card_deck) == 52

def test_deck_0002():
    """Tests to see if the deck deals 7 cards"""
    test_deck = Deck()
    test_hand = test_deck.deal_hand()
    assert len(test_hand) == 7

def test_deck_0003():
    """Tests to see if only one card is drawn"""
    test_deck = Deck()
    test_card = test_deck.draw_card()
    assert test_card == 'A'
