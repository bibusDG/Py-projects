import random

deck_colors = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
deck_cards = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
card_values = {}
full_deck = []

"""
Combine colors and cards together with "of" word for full deck of card
"""

for color in deck_colors:
    for card in deck_cards:
        full_deck.append(card + ' Of ' + color)

"""
Create dictionary with value for each card in deck
"""

for _ in range(4):
    STOP = 13
    for number in range(STOP):
        card_values[full_deck[number]] = values[number]
    full_deck = full_deck[STOP:]


def shuffle_dec():

    """
    Shuffle deck of cards randomly and create final playable deck -> final_game_deck
    """

    new_card_values = list(card_values.items())
    random.shuffle(new_card_values)
    final_game_dec = dict(new_card_values)
    return final_game_dec


playable_deck = shuffle_dec()


class Player:

    """
    Create class player
    :money_to_win - total amount of money you can win in one play
    """

    money_to_win = 0

    def __init__(self, name, cards, cards_value=0, actual_money=500, decision_maker=1):

        """
        :param name: players name
        :param cards: cards on hand and its value (e.g. [Jack of Hearts --> 10, Two of Diamonds --> 2]
        :param actual_money: actual money player posses
        :param cards_value: value of all cards in hands (e.g. Ace + Jack = 21, Jack + 2 = 12)
        :param decision_maker: gives the information if player want to take extra card or not
        """
        self.name = name
        self.cards = cards
        self.actual_money = actual_money
        self.cards_value = cards_value
        self.decision_maker = decision_maker

    def bet(self):

        """
        Function for making a bet
        """
        if self.actual_money > 0:
            while True:
                try:
                    print(self.name + ' You have ' + str(self.actual_money) + '$.')
                    value_of_bet = int(input('How much $ would You like to bet? : '))
                    if value_of_bet <= self.actual_money:
                        self.actual_money = self.actual_money - value_of_bet
                        Player.money_to_win += value_of_bet
                        break
                    else:
                        print('Not enough money. Try again.')
                except ValueError:
                    print('Please insert correct value')
                print()
        else:
            print(self.name + " You don't have money. You have lost a game!! Maybe next time :) \n")

    def auto_bet(self):

        """
        Function to get random bet from our croupier.
        """
        if self.actual_money >= 5:
            value_of_bet = random.randrange(1, self.actual_money + 1, 1)
            self.actual_money -= value_of_bet
            Player.money_to_win += value_of_bet
            print(self.name + ' bet is equal to ' + str(value_of_bet) + ' $. ' + self.name + ' still have ' +
                  str(self.actual_money) + '$.\n')
        else:
            print(self.name + ' have no more money. ')

    def deal(self):

        """
        Adding card to players hand and total value of all cards
        """

        self.cards.append(list(playable_deck.keys())[0] + ' -> ' + str(list(playable_deck.values())[0]))
        self.cards_value += list(playable_deck.values())[0]
        playable_deck.pop(list(playable_deck.keys())[0])


auto_player = Player('Leopold', [])
players_dict = {}


def list_of_players():

    """
    Create list of players and assign all to class Player
    """
    while True:
        try:
            players_number = int(input('How many players will play (from 1 to 5): '))
            if players_number in range(0, 6):
                break
            else:
                print('Please insert correct value.')
        except ValueError:
            print('Please insert correct value.')
    for _ in range(1, players_number+1):
        player = input('Please provide name of player ' + str(_) + ': ')
        players_dict['player' + str(_)] = Player(player, [])
    print()


def player_name():

    """
    Return all names of players in class Player
    """
    for player in players_dict.keys():
        yield players_dict[player]


def croupier_random_cards():

    """
    Our croupier is taking randomly 2 cards from deck
    """

    print('Hi, my name is ' + auto_player.name + '. I will be Your croupier.')
    print('I will take 2 random cards from deck. One will be covered.\n')
    auto_player.deal()
    auto_player.deal()
    print(auto_player.name + ' have ' + auto_player.cards[0])


def random_two_card_for_each():

    """
    Each player is getting two random cards from deck to start play
    """
    for player in player_name():
        player.deal()
        player.deal()
        print(player.name + ' cards are: ' + str(player.cards)
              + '  Total card value is ' + str(player.cards_value))


def croupier_decisions_for_cards():

    """
    Croupier decides how many card he will take
    """

    while auto_player.cards_value < 15:
        auto_player.deal()


def clean_hands():

    """
    Reset values (card, card_value, decision_maker etc.) to beginning values for next round
    """

    for player in player_name():
        player.cards = []
        player.cards_value = 0
        player.decision_maker = 1

    auto_player.cards = []
    auto_player.cards_value = 0
    Player.money_to_win = 0


players_without_money = []


def _round():

    """
    Game steps for each round
    """
    clean_hands()
    shuffle_dec()
    croupier_random_cards()
    random_two_card_for_each()
    auto_player.auto_bet()
    croupier_decisions_for_cards()

    for player in player_name():
        if player.actual_money == 0:
            print(player.name + ' You are out of money. You can not play. ')
            players_without_money.append(1)
        else:
            if player.cards_value < 22:
                player.bet()
                print('You can win ' + str(Player.money_to_win) + '\n')
                while player.decision_maker != 0:
                    print(player.name + ' Your cards are ' + str(player.cards) + ' with total value of '
                          + str(player.cards_value))
                    while True:
                        additional_card = input(player.name + ' do You want an extra card (y/n) ? :  ')
                        if additional_card == 'y' or additional_card == 'n':
                            break
                        else:
                            print('Please insert correct value.')
                        print()
                    if additional_card == 'y':
                        player.deal()
                        if player.cards_value > 21:
                            print(player.name + ' have more, than 21. You are out of this round.')
                            player.decision_maker = 0
                    else:
                        player.decision_maker = 0
            else:
                print(player.name + ' is not playing. To much points')


def round_result_split_money():

    """
    Result of round and splitting money between players
    """

    winners = dict()
    value = player_name()
    first_player = next(value)
    if first_player.cards_value < 22 and first_player.actual_money > 0:
        winners[first_player] = first_player.name

    for player in player_name():
        if player.cards_value < 22 and player.actual_money > 0:
            print(player.name + ' Your cards are ' + str(player.cards) +
                  ' with total value of ' + str(player.cards_value))
            if player.name not in winners.values() and 21 - player.cards_value < 21 - first_player.cards_value:
                winners.clear()
                first_player = player
                winners[first_player] = player.cards_value
            if player.name not in winners.keys() and 21 - player.cards_value == 21 - first_player.cards_value:
                winners[first_player] = player.cards_value

    print(auto_player.name + ' Your cards are ' + str(auto_player.cards) +
          ' with total value of ' + str(auto_player.cards_value) + '\n')

    if len(winners) == 0:
        if auto_player.cards_value > 21:
            print('Nobody wins')
        if auto_player.cards_value < 22:
            auto_player.actual_money += Player.money_to_win
            print(auto_player.name + ' is winning this round and have $' + str(auto_player.actual_money))

    if len(winners) > 0:
        if auto_player.cards_value > 21:
            print(auto_player.name + ' is loosing. To much points')
            win = int(Player.money_to_win / len(winners))
            for key in winners.keys():
                key.actual_money += win
                print(key.name + ' won this round. ' + key.name + ' have $' + str(key.actual_money))
        if auto_player.cards_value < 22 and auto_player.cards_value < int(list(winners.values())[0]):
            win = int(Player.money_to_win / len(winners))
            for key in winners.keys():
                key.actual_money += win
                print(key.name + ' won this round. ' + key.name + ' have $' + str(key.actual_money))
        if auto_player.cards_value < 22 and auto_player.cards_value > int(list(winners.values())[0]):
            win = int(Player.money_to_win)
            auto_player.actual_money += win
            print(auto_player.name + ' won this round. ' + auto_player.name + ' have $' + str(auto_player.actual_money))
        if auto_player.cards_value < 22 and auto_player.cards_value == int(list(winners.values())[0]):
            win = int(Player.money_to_win / len(winners) + 1)
            auto_player.actual_money += win
            print(auto_player.name + ' is winning this round and have $' + str(auto_player.actual_money))
            for key in winners.keys():
                key.actual_money += win
                print(key.name + ' is winning this round. ' + key.name + ' have $' + str(key.actual_money))


"""
Loop for game
"""

list_of_players()
yes = 1

while True:
    if len(playable_deck) < 5:
        print('End of game. Not enough cards')
        break
    if auto_player.actual_money <= 0:
        print('End of game. Croupier is out of money.')
        break
    if any(players_without_money):
        print('End of game. Players are out of money')
        break
    if yes == 0:
        print('Thanks for game. See You')
        break
    else:
        _round()
        print()
        round_result_split_money()
        while True:
            next_round = input('Next round (y/n) ?: ')
            if next_round == 'y' or next_round == 'n':
                break
            else:
                print('Please insert correct value.')
        if next_round == 'y':
            yes = 1
        else:
            yes = 0
