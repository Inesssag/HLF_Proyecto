import numpy as np
'''
Para jugar contra la máquina hay que crear tres tableros de 10x10.
En mi tablero colocaré mis barcos, en el de la máquina se colocarán de manera aleatoria.
Habrá un tablero visible en el que ver los resultados de los disparos
'''
tablero_mine = np.full((10,10), ' ')
tablero_maq = np.full((10,10),' ')
tablero_visible = np.full((10,10), '?')