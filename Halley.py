import random
import time

def halley():
    lista = []
    i = 1

    numero_cand = int(input('Inserisci il numero totale dei candidati: '))

    if numero_cand <=1:
        print("Il numero dei candidati è insufficiente. Riprova...")
        halley()

    while True:
        nome_cand = input('Inserisci il nome del ' + str(i) + ' candidato: ')

        i = i + 1
        lista.append(nome_cand)

        if numero_cand < i:
            break

    print('\nI candidati inseriti sono i seguenti: ', lista)

    print('Ora pescheremo il vincitore.')
    print('Attendere prego...')
    time.sleep(10)

    scelta_ran = random.choice(lista)
    print('\nIl vincitore è: ' + scelta_ran)

    itsfinish = input('\nVuoi far partire il programma di nuovo? S/N: ')

    if itsfinish == 'S' or itsfinish == 's':
        print('Attendere...')
        time.sleep(2)
        halley()

    elif itsfinish == 'N' or itsfinish == 'n':
        print('Attendere...')
        time.sleep(2)
        start()

def title():
    print('''   

 | |  | |     | | |           
 | |__| | __ _| | | ___ _   _ 
 |  __  |/ _` | | |/ _ \ | | |
 | |  | | (_| | | |  __/ |_| |
 |_|  |_|\__,_|_|_|\___|\__, |
                         __/ |
                        |___/   
   
    ''')
    time.sleep(1)

def start():
    scelta1 = int(input('''
------------------------------    
1) START
    
2) EXIT
------------------------------       
'''))

    if scelta1 == 1:
        print('Attendere...')
        time.sleep(2)
        halley()

    elif scelta1 == 2:
        scelta2 = input('Sei sicuro di voler uscire? S/N: ')

        if scelta2 == 'S' or scelta2 == 's':
            print('PROGRAMMA TERMINATO...')
            exit()

        elif scelta2 == 'N' or scelta2 == 'n':
            print('Attendere...')
            time.sleep(2)
            start()
title()
start()