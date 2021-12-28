from tkinter import *
from final_block_with_empty import *

button_dict = {}
names_list_value = {}
list_of_button = []

#------------------------------------------------------------------------

def get_button(name):

    """
    Get button function is changing color of button of blank place, so the user know in which place he changes
    the number
    """

    list_of_button.clear()
    list_of_button.append(name)
    logic()
    if len(list_of_button) > 0:
        for key in button_dict:
            if key == list_of_button[0]:
                button_dict[key].config(bg='yellow')
            else:
                button_dict[key].config(bg='white')

def new_window():

    """Creating playing game field with empty places to fill with active and disabled buttons"""

    window.destroy()
    new_window = Tk(className='Sudoku Game')
    new_window.geometry('1200x800')
    new_window.configure(bg = 'grey')


    def helper():

        """
        Help button. By pressing help button program changes the blank field into the number and helps to solve sudoku

        """

        button_dict[list_of_button[0]].config(text = new_list[int(list_of_button[0][1])][int(list_of_button[0][2])])
        button_dict[list_of_button[0]].config(state = DISABLED, bg = '#B4EAED')
        play_lista[int(list_of_button[0][1])][int(list_of_button[0][2])] = new_list[int(list_of_button[0][1])][int(list_of_button[0][2])]

    def sudoku_check():

        """
        Function responsible for checking ready sudoku. While user has finished sudoku, he can check if sudoku is
        solved in a right way
        :help_button -> visualization of help button
        :check_sudoku -> visualization of check sudoku button

        """

        play_lista_values = []
        lista_values = []
        for i in play_lista:
            for j in i:
                play_lista_values.append(j)
        for i in new_list:
            for j in i:
                lista_values.append(j)
        if play_lista_values == lista_values:
            great = Label(text='WELL DONE!!', bg='white', font=('Arial', 80))
            great.place(x=150, y=300)
            great.after(2000, great.destroy)
        else:
            busted = Label(text='BUSTED', bg='white', font=('Arial', 80))
            busted.place(x=200, y=300)
            busted.after(2000, busted.destroy)

    help_button = Button(new_window, text='HELP ME!!', font=('Arial', 25), command = helper, activebackground='green')
    help_button.pack(ipadx=200, ipady=10, expand=True)
    help_button.place(x=900, y=100)

    check_sudoku = Button(new_window, text='CHECK SUDOKU', font=('Arial', 25), command=sudoku_check, activebackground='green')
    check_sudoku.pack(ipadx=200, ipady=10, expand=True)
    check_sudoku.place(x=850, y=300)

    for i in range(9):
        for j in range(9):
            if play_lista[i][j] != '':
                Button(new_window, height=2, width=5, font=('Arial', 20), state=DISABLED, bg = 'white',
                        text=play_lista[i][j]).grid(row=i, column=j)
            else:
                button_dict['b' + str(i) + str(j)] = Button(new_window, height=2, width=5, font=('Arial', 20), bg = 'white',
                    state=NORMAL, text = '',command = lambda name = 'b' + str(i) + str(j): get_button(name))

    for key, values in button_dict.items():
        values.grid(row=int(list(key)[1]), column = int(list(key)[2]))

    if len(list_of_button) > 0:
        print(button_dict[list_of_button[0]])
        button_dict[list_of_button[0]].config(bg='green')

def logic():

    """
    Function responsible for implementing number on empty fields from 1 to 9
    """

    if list_of_button[0] not in names_list_value:
        names_list_value[list_of_button[0]] = 1
    else:
        if names_list_value[list_of_button[0]] < 9:
            names_list_value[list_of_button[0]] += 1
        else:
            names_list_value[list_of_button[0]] = 1
    button_dict[list_of_button[0]].config(text=names_list_value[list_of_button[0]])
    play_lista[int(list_of_button[0][1])][int(list_of_button[0][2])] = names_list_value[list_of_button[0]]

#---------------------------------------------------------------------------

def start_button():

    """
    Defining start button on main window
    """

    start_button = Button(window, text='PLAY SUDOKU', font=('Arial', 15), command=new_window, justify='center')
    start_button.pack(ipadx=100, ipady=10, expand=True)
    start_button.place(x=520, y=400)


def easy_button_choice():
    """
    Easy button color and choice of easy game
    """

    game_level('Easy')
    medium_button.config(bg = 'white')
    hard_button.config(bg = 'white')
    easy_button.config(bg = 'green')
    start_button()

def medium_button_choice():
    """
    Medium button color and choice of medium game
    """
    game_level('Medium')
    medium_button.config(bg = 'green')
    hard_button.config(bg = 'white')
    easy_button.config(bg = 'white')
    start_button()

def hard_button_choice():
    """
    Hard button color and choice of hard game
    """
    game_level('Hard')
    medium_button.config(bg='white')
    hard_button.config(bg='green')
    easy_button.config(bg='white')
    start_button()

"""
Tkinter windows for game
: window -> main menu window
"""


window = Tk(className='Sudoku Game')
window.geometry('1200x800')
window.configure(bg = 'grey')
game_promo = Label(text = 'WELCOME TO SUDOKU\nPLEASE CHOOSE LEVEL\n',  bg = 'grey', font =('Arial', 20))
game_promo.place(x=430, y=190)

easy_button = Button(window, text='EASY', font = ('Arial', 15), command = easy_button_choice)
easy_button.pack(ipadx=100, ipady=10, expand = True)
easy_button.place(x=420, y=300)

medium_button = Button(window, text='MEDIUM', font = ('Arial', 15), command = medium_button_choice)
medium_button.pack(ipadx=100, ipady=10, expand = True)
medium_button.place(x=550, y=300)

hard_button = Button(window, text='HARD', font = ('Arial', 15), command = hard_button_choice)
hard_button.pack(ipadx=100, ipady=10, expand = True)
hard_button.place(x=700, y=300)


exit_button = Button(window, text='EXIT', font = ('Arial', 15), command = lambda : window.quit(), justify='center')
exit_button.pack(ipadx=100, ipady=10, expand = True)
exit_button.place(x=570, y=450)



window.mainloop()