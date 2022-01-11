import string
import random

with open('C:\\Users\\gross\\PycharmProjects\\excersizes\\hangman\\words.csv') as f:
    lines = [line for line in f]

word = random.choice(lines).upper()
empty_word = ['_' for x in word]
provided_letters = []


def word_with_empty(letter):
    indexes_of_letter_in_word = [i for i, val in enumerate(word) if val == letter]
    for num in indexes_of_letter_in_word:
        empty_word[num] = word[num]


class Player:
    hangman = 'HANGMAN'

    def __init__(self, name, letters='_______', counter=0):
        self.name = name
        self.letters = letters
        self.counter = counter

    def choose_a_letter(self):
        letter = input(self.name + ' please input your letter: ')
        while letter not in string.ascii_letters:
            print('You need to use letters')
            letter = input(self.name + ' please input your letter: ')
        else:
            provided_letters.append(letter.upper())
            return letter.upper()

    def wrong_answer(self):
        self.counter += 1
        print('Wrong Answer ' + self.name + '. Yor HANGMAN letters are: ', end="")
        self.letters = Player.hangman[0:self.counter] + self.letters[self.counter:]
        print(self.letters)
        print()

    def good_answer(self):

        print('Nice!! Your letter is in word. Please continue ' + self.name)
        word_with_empty(provided_letters[-1])
        print()


player1 = input('Insert Player1 name: ')
pl1 = Player(player1)
player2 = input('Insert Player2 name: ')
pl2 = Player(player2)
print()


def game_play(player, name):

    print(name + ' it is Your move')
    print('Word we are guessing is:  ' + ''.join(empty_word))
    if player.choose_a_letter() not in word:
        player.wrong_answer()
        if player.letters == Player.hangman:
            print(player.name + ' is loosing game!!')
            print('Hidden word was: ' + word)
        else:
            if name == pl1.name:
                game_play(pl2, pl2.name)
            if name == pl2.name:
                game_play(pl1, pl1.name)
    else:
        player.good_answer()
        if "".join(empty_word).upper() == word:
            print('Well done ' + player.name + '. You are a WINNER!!')
        else:
            if name == pl1.name:
                game_play(pl1, pl1.name)
            if name == pl2.name:
                game_play(pl2, pl2.name)


game_play(pl1, pl1.name)
