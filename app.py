"""Entry point for the application"""
from cards.deck import Deck
from cards.hand import Hand


def main():
    """Entry point for the application"""
    print('Hello world')
    game_deck = Deck()
    human_player = Hand()
    computer_player = Hand()
    game_deck.shuffle()
    game_over = False

    human_player.cards = game_deck.deal_hand()
    computer_player.cards = game_deck.deal_hand()

    while not game_over:

        player_card_selection = input(f'Please choose a card from your hand you have the following: {human_player}')
        print(f'Computer has: {computer_player}')  # delete me later
        players_turn = True
        while players_turn:
            while not human_player.check_if_in_hand(player_card_selection.upper()):
                print(f'{player_card_selection} not in hand.')
                player_card_selection = input(
                    f'Please choose a card from your hand you have the following: {human_player}')
                print(f'Computer has: {computer_player}')  # delete me later

            if computer_player.check_if_in_hand(player_card_selection.upper()):
                print(f'Computer has those cards!')
                human_player.cards = computer_player.draw_card(player_card_selection, human_player.cards)
            else:
                print('Go fish!')
                human_player.cards.append(game_deck.draw_card())
                players_turn = False

    print(human_player)
    print(computer_player)


main()
