import random

lists = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

lista = []
play_lista = []
used_list = []

for i in range(0, 9):
    lista.append([0] * 9)

#-------------------------------------------------------------

def build_a_squares(number):

    """"
    Creatng squares 3x3 for sudoku table.
    """

    all_squares = []
    k = 0
    l = 0
    counter = 0
    list_of_squares = []
    while counter != 9:
        for l in range(0, 7, 3):
            for i in range(k, k + 3):
                list_of_squares += lista[i][l:l + 3]
            all_squares.append(list_of_squares)
            list_of_squares = []
            counter += 1
        k += 3
    return all_squares[number]

#-----------------------------------------------------------------

def values_in_table(k_step, l_step, list_name):

    """
    Creating values in sudoku table
    :param k_step: i value
    :param l_step: numbers from 0 to 2
    :param list_name: number of list from lists = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    :return:
    """

    new_value = random.choice(list_name)
    if new_value not in build_a_squares(0) and new_value not in lista[k_step]:
        new_list = [x for x in range(new_value, 10)] + [x for x in range(1, new_value)]
        list_name.remove(new_value)
        i = 0
        for k in range(0 + k_step, 7 + k_step, 3):
            for l in range(l_step, 9, 3):
                lista[k][l] = new_list[i]
                i += 1

#--------------------------------------------------------------------

random.shuffle(lists)

def first():
    for i in range(3):
        values_in_table(0, i, lists[0])
def second():
    for i in range(3):
        values_in_table(1, i, lists[1])
def third():
    for i in range(3):
        values_in_table(2, i, lists[2])

first()
second()
third()

for k in lista:
    play_lista.append(k)
    used_list += k

