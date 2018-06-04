#Ciao Cau

import random

Domanda = input('Vuoi tirare il dado? [s/n]?\n')

while Domanda != 'n':
    if Domanda == 's':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(die1, die2)
        Domanda = input('Vuoi tirare di nuovo il dado? [s/n]?\n')
    else:
        print('Errore! Digita "s" o "n".')
        Domanda = input('Vuoi tirare il dado? [s/n]?\n')        
