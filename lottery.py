import random
liczba = int(random.randint(0,101))
print(liczba)
counter = 0
lista = []
while True:
    losowa = int(input('Wylosowano liczbę. Podaj ją i spróbój zgadnąc jaka to liczba: '))
    if losowa < 1 or losowa > 100:
        print('Poza zakresem')
        continue
    elif losowa == liczba:
        counter += 1
        print('Gratulacje, to ta liczba!!. Zgadłeś za ' + str(counter) + ' razem')
        break
    if len(lista) == 0:
        if abs(losowa - liczba) < 10:
            print("Warm")
            lista.append(losowa)
            counter += 1
        else:
            print('Cold')
            lista.append(losowa)
            counter +=1
    else:
        if abs(losowa - liczba) < abs(lista[-counter] - liczba):
            print('WARMER')
            lista.append(losowa)
            counter += 1
        else:
            print('Colder')
            lista.append(losowa)
            counter += 1
    print(counter)
    print(lista)



