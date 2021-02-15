"""Entry point for the application"""
from cards.deck import Deck
from cards.hand import Hand
import random


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

        print(f'Computer has: {computer_player}')  # delete me later
        players_turn = True
        while players_turn:
            player_card_selection = input(f'Please choose a card from your hand you have the following: {human_player}')
            while not human_player.check_if_in_hand(player_card_selection.upper()):
                print(f'{player_card_selection} not in hand.')
                player_card_selection = input(
                    f'Please choose a card from your hand you have the following: {human_player}')
                print(f'Computer has: {computer_player}')  # delete me later

            if computer_player.check_if_in_hand(player_card_selection.upper()):
                print(f'Computer has those cards!')
                human_player.cards = computer_player.draw_card(player_card_selection, human_player.cards)
                human_player.book_check(player_card_selection)
            else:
                print('Go fish!')
                drawn_card = game_deck.draw_card()
                human_player.cards.append(drawn_card)
                human_player.book_check(drawn_card)
                players_turn = False

        while not players_turn:
            computer_card_selection = random.choice(computer_player.cards)
            if human_player.check_if_in_hand(computer_card_selection):
                print(f'Computer guessed {computer_card_selection} and got it right!')
                computer_player.cards = human_player.draw_card(computer_card_selection, computer_player.cards)
                computer_player.book_check(computer_card_selection)
            else:
                drawn_card = game_deck.draw_card()
                computer_player.cards.append(drawn_card)
                computer_player.book_check(drawn_card)
                print(f'Computer guessed {computer_card_selection} and got it wrong!\n It is now your turn!')
                players_turn = True

    print(human_player)
    print(computer_player)


main()
