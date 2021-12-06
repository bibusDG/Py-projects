# ***********INPUTS**********************************************

filepath = "C:\\"
f = open(filepath, "r")
list_of_lists = [(line.strip()).split() for line in f]          # opearcje na pliku wejściowym


n = int(list_of_lists[0][0])

_in = [int(k) for k in list_of_lists[2]]
_out = [int(k) for k in list_of_lists[3]]               # listy danych wejściowych bazujących na pliku wejściowym
weight = [int(k) for k in list_of_lists[1]]
check_point = {}


# **********************************************


min_mass_overall = 6500     # minimalna waga
mass_of_cycle = 0           # masa pojedynczego cyklu
leng_of_cycle = 0           # długość cyklu
final_cost = 0              # finalna wartość/waga zamiany


#**********************************************

in_vs_out = {}
for i, val in enumerate(_out):    # utworzenie słownika relacji wejście/wyjście
    in_vs_out[val] = _in[i]


# ***********************************************

mass_of_each_ele = {}
for i, val in enumerate(weight):            # utworzenie słownika relacji numer słonia -> waga słonia
    mass_of_each_ele[i + 1] = weight[i]

# ***********************************************

for i in range(n):
    indeks = in_vs_out[_out[i]]
    while indeks not in check_point:
        check_point[indeks] = indeks                                # utowrzenie cyklów prostych
        indeks = in_vs_out[indeks]
        leng_of_cycle += 1
        mass_of_cycle += mass_of_each_ele[indeks]
        min_mass_overall = min(mass_of_each_ele[indeks], min_mass_overall)

    if leng_of_cycle > 0:
        metod1 = mass_of_cycle + (leng_of_cycle - 2) * min_mass_overall
        metod2 = mass_of_cycle + min_mass_overall + (leng_of_cycle + 1) * min(weight)  #porównanie metod
        final_cost += min(metod1, metod2)



    cycle = []
    mass_of_cycle = 0
    leng_of_cycle = 0                   # zerowanie wartości dla każdego cyklu
    min_mass_overall = 6500

print(final_cost)                   # wydruk finalnej wagi



