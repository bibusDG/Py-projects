from sudoku_table_creator import *
import numpy as np

new_list = np.array_split(used_list, 9)

def game_level(level):

    """"
    Creating table with empty spots and choose game level: easy, medium, hard
    : Hard -> cuts randomly from 5 to 8 squares in each row
    : Medium -> cuts randomly from 4 to 6 squares in each row
    : easy -> cuts randomly form 2 to 5 squares in each row

    """

    if level == 'Hard':
        for i in play_lista:
            z = random.randint(5, 8)
            s = random.sample(range(0, 9), z)
            for k in s:
                i[k] = ''

    if level == 'Medium':
        for i in play_lista:
            z = random.randint(4, 6)
            s = random.sample(range(0, 9), z)
            for k in s:
                i[k] = ''

    if level == 'Easy':
        for i in play_lista:
            z = random.randint(2, 5)
            s = random.sample(range(0, 9), z)
            for k in s:
                i[k] = ''

    return play_lista


