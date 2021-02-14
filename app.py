"""Entry point for the application"""
from cards.deck import Deck
from cards.hand import Hand


def main():
    """Entry point for the application"""
    print('Hello world')
    game_deck = Deck()
    player = Hand()
    computer_player = Hand()
    game_deck.shuffle()
    game_over = False

    player.cards = game_deck.deal_hand()
    computer_player.cards = game_deck.deal_hand()

    while not game_over:

        player_card_selection = input(f'Please choose a card from your hand you have the following: {player}')
        while not player.check_if_in_hand(player_card_selection):
            print(f'{player_card_selection} not in hand.')
            player_card_selection = input(f'Please choose a card from your hand you have the following: {player}')

        print('Yes')

    print(game_deck)
    print(computer_player)


main()
