# TICTACTOE

# PATTERN

empty = {'row1': ['_1_|', '_2_|', '_3_'], 'row2': ['_4_|', '_5_|', '_6_'], 'row3': [' 7 |',' 8 |', ' 9 ']}
listaX = {'row1': ['_x_|', '_x_|', '_x_'], 'row2': ['_x_|', '_x_|', '_x_'], 'row3': [' x |', ' x |', ' x ']}
listao = {'row1': ['_o_|', '_o_|', '_o_'], 'row2': ['_o_|', '_o_|', '_o_'], 'row3': [' o |', ' o |', ' o ']}

def TICTACTOE():
    for a in empty.values():
        print("".join(a))

print('To jest plansza do gry:')
TICTACTOE()

choice = str(input('Wybierz czym chcesz grać o czy x ?: '))
lista = ["x", 'o']

# Wybór miejsca ox *************************************************************

def oxchoice():
    global place
    global row
    global minus
    place = int(input('Podaj miejsce dla ' + choice + ': '))
    if place in range(0, 4):
        minus = 1
        row = 'row1'
        error_check()
    elif place in range(4, 7):
        minus = 4
        row = 'row2'
        error_check()
    else:
        minus = 7
        row = 'row3'
        error_check()

# Sprawdzenie błedu i lokalizacji o,x*************************************************************

def error_check():
    if empty[row][place - minus][1] not in lista:
        empty[row][place - minus] = z[row][place - minus]
    else:
        print('Niewłaściwe miejsce!!!')
        oxchoice()


#*****************************************************************
def pion():
    lista_pion = []
    for i in range(3):
       for a in empty.values():
           lista_pion.append(a[i][1])
    #print("".join(lista_pion))

    lista_poziom = []
    for a in empty:
        for i in range(3):
            lista_poziom.append(empty[a][i][1])

    lista_skos1 = []
    x=0
    for a in empty:
        lista_skos1.append(empty[a][x][1])
        x+=1
    #print(lista_skos1)

    lista_skos2 = []
    x = 2
    for a in empty:
        lista_skos2.append(empty[a][x][1])
        x -= 1
    #print(lista_skos2)
    lista_pion2 = []
    lista_pion2.append(lista_pion)
    lista_pion2.append(lista_poziom)
    lista_pion2.append(lista_skos1)
    lista_pion2.append(lista_skos2)

    final = ",".join(["".join(x) for x in lista_pion2])
    return(final)

# Pętla gry *****************************************************************************************

while True:
    if 'xxx' in pion():
        print('wygrały x !!!')
        break
    elif 'ooo' in pion():
        print('wygrały o !!')
        break
    elif choice == 'x':
        pion()
        z = listaX
        oxchoice()
        TICTACTOE()
        choice = 'o'
        #print(empty)
    elif choice == 'o':
        z = listao
        oxchoice()
        TICTACTOE()
        choice = 'x'
    else:
         print('Wybierz x lub o: ')

