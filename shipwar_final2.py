alpha = 'ABCDEFGHIJ'
N = 10
start_list = {4:1, 3:1, 2:0, 1:2}
ship_list = {4:1, 3:1, 2:0, 1:2}
player1_ships_positions = []
player2_ships_positions = []
numbers = [str(i) for i in range(1, N+1)]
numbers_letters = []
for i in alpha:
    for j in numbers:
        numbers_letters.append(i+j)


#---------------------------------------------------------------

lista = []
row1 = []
help_row = []
for i in range(N):
    row1.append(['0 '] * N)
    help_row.append([0]*N)

row2 = []
for j in range(N):
    row2.append(['0 '] * N)

help_row2 = []
for i in range(N):
    help_row2.append([0]*N)


#-----------------------------------------------------------------

def table_with_letters(_list, N):
    for j in range(N):
        print(j+1, end= '  ')
    print()
    k = 0
    while k != N:
        print(' '.join(_list[k]), alpha[k])
        k += 1


#--------------------------------------------------------------------

sample = []
for i in range(N):
    sample.append(['0 '] * N)
table_with_letters(sample , N)

# ---------------------------------------------------------------------

def check_zero():
    # lista = []
    if ship_orient == "H"  and int(ship_localization[1:]) + int(ship_size) < 12:
        for i in range(ship_size):
            if help_row[alpha.index(ship_localization[0])][int(ship_localization[1:])-1+i] == 0:
                lista.append(1)

    if ship_orient == "V" and alpha.index(ship_localization[0]) + ship_size < 11:
        for i in range(ship_size):
            if help_row[alpha.index(ship_localization[0])+i][int(ship_localization[1:])-1] == 0:
                lista.append(1)

    return len(lista) == ship_size

#------------------------------------------------------

def check_possibility():
    if ship_orient == "H" and check_zero():
        for i in range(-1, 2):
            for j in range(int(ship_localization[1:]) - 2, ship_size + int(ship_localization[1:])):
                help_row[alpha.index(ship_localization[0]) + i][j] = 1

    if ship_orient == 'V' and check_zero():
        for j in range(alpha.index(ship_localization[0]) - 1, ship_size + alpha.index(ship_localization[0]) + 1):
            for i in range(-1, 2):
                help_row[j][int(ship_localization[1:]) - 1 + i] = 1

    return help_row

#--------------------------------------------------------------------------

def ships_amount(ship_size):
    if ship_list[ship_size] > 0:
        ship_list[ship_size] = ship_list[ship_size]-1
        Ship.ship_counter -= 1
        print('You have ' + str(ship_list))
        return ship_list[ship_size] >= 0

#----------------------------------------------------------

class Ship:

    ship_counter = 4
    k = row1

    def __init__(self, size, orient, localization):
        self.size = size
        self.orient = orient
        self.localization = localization


    def build_ship(self):
        if self.orient == "H":
            for j in range(int(ship_localization[1:])-1, ship_size+int(ship_localization[1:])-1):
                Ship.k[alpha.index(ship_localization[0])][j] = "# "
            return table_with_letters(Ship.k, N)


        elif self.orient == 'V':
            for j in range(alpha.index(ship_localization[0]), ship_size + alpha.index(ship_localization[0])):
                Ship.k[j][int(ship_localization[1:]) - 1] = '# '
            return table_with_letters(Ship.k, N)

#-------------------------------------------------------------------------------------

def ship_in_list():
    if ship_orient == 'H' and players ==2:
        single_ship = [str(ship_localization[0]) + str(i) for i in range(int(ship_localization[1:]), ship_size+int(ship_localization[1:]))]
        player1_ships_positions.append(single_ship)
    if ship_orient == 'V' and players == 2:
        single_ship = [str(alpha[alpha.index(ship_localization[0])+i]) + str(ship_localization[1:]) for i in range(ship_size)]
        player1_ships_positions.append(single_ship)
    if ship_orient == 'H' and players == 1:
        single_ship = [str(ship_localization[0]) + str(i) for i in
                       range(int(ship_localization[1:]), ship_size + int(ship_localization[1:]))]
        player2_ships_positions.append(single_ship)
    if ship_orient == 'V' and players == 1:
        single_ship = [str(alpha[alpha.index(ship_localization[0]) + i]) + str(ship_localization[1:]) for i in
                       range(ship_size)]
        player2_ships_positions.append(single_ship)


#-------------------------------------------------------------------------------------

def check_the_ship(ship_position):
    for i in ship_position:
        if shot in i and i.count('0 ') != len(i)-1:
            i[i.index(shot)] = '0 '
            print('Well done!! You have shoot ' + str(len(i)))
            print('You still need to shoot ' + str(len(i) - i.count('0 ')) + ' times to sink this ship.')
        elif shot in i and i.count('0 ') == len(i)-1:
            print('Ship ' + str(len(i)) + ' destroyed!!')



#--------------------------------------------------------------------------------------
ship_size_list = ['4', '3', '2', '1']
direction_list = ["H", "V"]
players = 2
while players != 0:
    while Ship.ship_counter != 0:
        print('You have these ships: ' + str(ship_list))
        ship_size = input('Choose a type of ship You want to use!! : ')
        while ship_size not in ship_size_list:
            ship_size = input('Choose a type of ship You want to use!! : ')
        ship_size = int(ship_size)
        if ships_amount(ship_size):
            ship_orient = input("Give ship orentation H:horizontal, V:vertical : ")
            while ship_orient not in direction_list:
                ship_orient = input("Give ship orentation H:horizontal, V:vertical : ")
            ship_localization = input("Give position of ship i.e C4 :  ")

            while ship_localization not in numbers_letters:
                 ship_localization = input("Give position of ship i.e C4 :  ")
            ship = Ship(ship_size, ship_orient, ship_localization)
            if check_zero():
                check_possibility()
                ship.build_ship()
                lista = []
                ship_in_list()
            else:
                print('Ship <-> Ship or Ship <-> Land collision')
                ship_list[ship_size] += 1
                Ship.ship_counter += 1
        else:
            print('Choose another ship')
    if players == 2:
        print('Player one finished putting ships onto field ')
        print()
        print('Player 2 table')


    Ship.k = row2
    # lista = []
    Ship.ship_counter = 4
    players -=1
    ship_list = start_list
    help_row = help_row2



print('Player two finished putting ships onto field: ')
ship_in_list()
print()
print()

#---------------------------SHOOTING------------------------------

class Player_Fields:
    def __init__(self, player_name, shots, row, result):
        self.player_name = player_name
        self.shots = shots
        self.row = row
        self.result = result
    def game_field(self):
        for i in range(N):
            self.row.append(['0 '] * N)
        table_with_letters(self.row, N)

player1 = Player_Fields('P1', 9, [], 0)
player2 = Player_Fields('P2', 9, [], 0)
player_list = ['P1', 'P2']
print('Time to shoot. Each of You have 9 shots. Winner is person,  who will')
print('have more destroyed ships during game.')
player_name = str(input('Choose who will start. Player One (P1) or Player Two (P2): '))
while player_name not in player_list:
    player_name = str(input('Choose who will start. Player One (P1) or Player Two (P2): '))


#---------------------------------------------------------------------------------

def check_true(ship_position):
    for i in ship_position:
        if shot in i:
            return True

def shot_making(play):
    play.game_field()
    global shot
    shot = input(('You have ' + str(play.shots) + ' shoots . Choose a field to shoot: '))
    while shot not in numbers_letters:
        shot = input(('You have ' + str(play.shots) + ' shoots . Choose a field to shoot: '))
    play.shots -= 1


#---------------------------------------------------------------------------------

def shooting_game(play, ships_positions, row_type):
    if row_type[alpha.index(shot[0])][int(shot[1:]) - 1] == "# ":
        play.row[alpha.index(shot[0])][int(shot[1:]) - 1] = "X "
        play.result += 1
        play.game_field()
        check_the_ship(ships_positions)

def missed_shot(play):
    print('You missed. Maybe next time')
    play.row[alpha.index(shot[0])][int(shot[1:]) - 1] = "* "


def P1_game():
    while player1.result != 9:
        if player1.shots > 0:
            shot_making(player1)
            if check_true(player2_ships_positions):
                shooting_game(player1, player2_ships_positions, row2)
                P1_game()
            else:
                missed_shot(player1)
                player_name = 'P2'
                print(player_name)
                if player2.shots > 0:
                    P2_game()
        # else:
        #     print()
        elif player2.shots > 0:
            print('Out of shots!!. Player 2 turn')
            P2_game()
        else:
            break


def P2_game():
    while player2.result != 9:
        if player2.shots > 0:
            shot_making(player2)
            if check_true(player1_ships_positions):
                shooting_game(player2, player1_ships_positions, row1)
                P2_game()
            else:
                missed_shot(player2)
                player_name = 'P1'
                print(player_name)
                if player1.shots > 0:
                    P1_game()
        # else:
        #     print()
        elif player1.shots > 0:
            print('Out of shots!!. Player 1 turn.')
            P1_game()
        else:
            break

if player_name == 'P1' and player1.shots > 0:
    P1_game()
elif player_name == 'P2' and player2.shots > 0:
    P2_game()
if player1.result == 9 or player2.result == 9 or player1.shots == 0 or player2.shots == 0 :
    print('Game over.')
    print('These are resuts of war: ')
    print('Player 1 have: ' + str(player1.result) + ' points')
    print('Player 2 have: ' + str(player2.result) + ' points')
if player1.result > player2.result:
    print('Player 1 is a WINNER!! GRATS !!!!')
elif player1.result < player2.result:
    print('Player 2 is a WINNER!! GRATS !!!!')
else:
    print('No Winner')
