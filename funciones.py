import numpy as np
import time
import variables as var


# Inicializar los tableros
# np.full() crea una matriz que es asignada a la variable tablero.mine. Con 'fill' se indica con qué se llena al
# llamar a la función
def init_tablero_mine(fill):
    var.tablero_mine = np.full((10,10),' ')
    print('Bienvenido al juego de hundir la flota')

# Tablero máquina (oculto)
def init_tablero_maq(fill):
    var.tablero_maq = np.full((10,10),' ')

# Tablero basado en el de la máquina pero visible.
def init_tablero_visible(fill):
    var.tablero_visible = np.full((10,10),'?')

# Para generar los barcos se establece dos opciones, los que genera la máquina(aleatorios) y los que colocas tú(manual)
# Por defecto asigno el tablero aleatorio y en la primera condición indico que en caso contrario, elijo la orientación.
def generar_barco_simple (tablero,eslora,tablero_aleat=True):
    if tablero_aleat:
        orientacion = np.random.choice(['N','S','E','W'])
    
    else:
        orientacion = input('Introduce uno de estos: N, S, E, W')
#En cualquiera de los casos, si sale la orientación E: se indican las coord (aleat. o no) y compruebo que no sale del tablero
    if orientacion == 'E':
        
        while True:
            if tablero_aleat:
                barco_x = np.random.randint(0,10)
                barco_y = np.random.randint(0,10)

            else:
                barco_x = int(input('Introduce una coordenada X entre 0 y 9 inclusive'))
                barco_y = int(input('Introduce una coordenada Y entre 0 y 9 inclusive'))
#Como la orientación es este, se comprueba que la coordenada y es menor que 10 menos lo que mide el barco
# y que hay hueco en el tablero.
#Con all indico que sea True todo lo que aparece dentro y en caso de que lo sea, en el tablero que se marcará "O"
            if barco_y <= (10-eslora) and all(hueco != 'O' for hueco in tablero[barco_x , barco_y : barco_y + eslora]):
                tablero[barco_x , barco_y : barco_y + eslora] = 'O'
                break
    
    elif orientacion == 'W':

        while True:
            if tablero_aleat:
                barco_x = np.random.randint(0,10)
                barco_y = np.random.randint(0,10)

            else:
                barco_x = int(input('Introduce una coordenada X entre 0 y 9 inclusive'))
                barco_y = int(input('Introduce una coordenada Y entre 0 y 9 inclusive'))
#En este caso la orientación es oeste(izda) indicaría lo contrario que en el caso de E.
            if barco_y >= (eslora-1) and all(hueco != 'O' for hueco in tablero[barco_x, barco_y - eslora : barco_y]):
                tablero[barco_x, barco_y - eslora : barco_y] = 'O'
                break

    elif orientacion == 'N':
        
        while True:
            if tablero_aleat:
                barco_x = np.random.randint(0,10)
                barco_y = np.random.randint(0,10)

            else:
                barco_x = int(input('Introduce una coordenada X entre 0 y 9 inclusive'))
                barco_y = int(input('Introduce una coordenada Y entre 0 y 9 inclusive'))
#En el caso de N(hacia arriba), se tiene en cuenta el eje x por ser el vertical.             
            if barco_x >= (eslora-1) and all(hueco != 'O' for hueco in tablero[barco_x - eslora : barco_x, barco_y]):
                tablero[barco_x - eslora : barco_x, barco_y] = 'O'
                break
        
    elif orientacion == 'S':

        while True:
            if tablero_aleat:
                barco_x = np.random.randint(0,10)
                barco_y = np.random.randint(0,10)

            else:
                barco_x = int(input('Introduce una coordenada X entre 0 y 9 inclusive'))
                barco_y = int(input('Introduce una coordenada Y entre 0 y 9 inclusive'))

            if barco_x <= (10-eslora) and all(hueco != 'O' for hueco in tablero[barco_x : barco_x + eslora, barco_y]):
                tablero[barco_x : barco_x + eslora, barco_y] = 'O'
                break
    

#Los barcos propios que se generan tiene en cuenta el nº de cada tipo de barco.
#Simplemente llamo a la función genérica mencionada antes y le indico que el tablero es el mio, la eslora e indico que no se genere la función de forma aleatoria.
def generar_todos_los_barcos_mios():
    cantidad_barcos_4_eslora = 1
    cantidad_barcos_3_eslora = 2
    cantidad_barcos_2_eslora = 3
    cantidad_barcos_1_eslora = 4
    
    for _ in range(cantidad_barcos_4_eslora):
        print('Introduce las coordenadas de tu barco de 4 de eslora')
        generar_barco_simple(var.tablero_mine,4,tablero_aleat=False)
        print(var.tablero_mine)
#Con el range se repite el nº de veces que barcos tiene.
    for _ in range(cantidad_barcos_3_eslora):
        print('Introduce las coordenadas de tu barco de 3 de eslora')
        generar_barco_simple(var.tablero_mine,3,tablero_aleat=False)
        print(var.tablero_mine)

    for _ in range(cantidad_barcos_2_eslora):
        print('Introduce las coordenadas de tu barco de 2 de eslora')
        generar_barco_simple(var.tablero_mine,2,tablero_aleat=False)
        print(var.tablero_mine)

    for _ in range(cantidad_barcos_1_eslora):
        print('Introduce las coordenadas de tu barco de 1 de eslora')
        generar_barco_simple(var.tablero_mine,1,tablero_aleat=False)
        print(var.tablero_mine)

# Ahora lo mismo pero al ser la máquina, se generará de forma aleatoria.
def generar_todos_los_barcos_maquina():
    cantidad_barcos_4_eslora = 1
    cantidad_barcos_3_eslora = 2
    cantidad_barcos_2_eslora = 3
    cantidad_barcos_1_eslora = 4
    
    for _ in range(cantidad_barcos_4_eslora):
        generar_barco_simple(var.tablero_maq,4,tablero_aleat=True)

    for _ in range(cantidad_barcos_3_eslora):
        generar_barco_simple(var.tablero_maq,3,tablero_aleat=True)

    for _ in range(cantidad_barcos_2_eslora):
        generar_barco_simple(var.tablero_maq,2,tablero_aleat=True)

    for _ in range(cantidad_barcos_1_eslora):
        generar_barco_simple(var.tablero_maq,1,tablero_aleat=True)

# Al igual que he creado los barcos con una función común que luego he aplicado a casos concretos, que hecho lo mismo con le función disparar.
# Serán los tres tableros los que se deberán modificar.
def disparar (tablero_mine,tablero_maq,tablero_visible):
    print('Comienza el juego. Primero juegas tú. Si aciertas te tocará otra vez. Si fallas jugará la máquina')
    turno_jugador = True
    #Para empezar jugando tú

    while True:

        if turno_jugador == True:
            
            if 'O' in tablero_maq:
                disparo_mio_x = int(input('Introduce la coordenada X de tu disparo: [0,9]'))
                disparo_mio_y = int(input('Introduce la coordenada Y de tu disparo: [0,9]'))
#Si hay barcos colocados en el tablero de la maq, se introducen las coord del disparo.                
#Si en esa coord, en el tablero de la maq hay 'O', entonces se cambia por 'X' en ese mismo tablero y se muestra el visible.                
                if tablero_maq[disparo_mio_x, disparo_mio_y] == "O":
                    tablero_maq[disparo_mio_x, disparo_mio_y] = "X"
                    tablero_visible[disparo_mio_x, disparo_mio_y] = 'X'
                    print('BARCO TOCADO!')
                    print(tablero_visible)
                    print('\n')
#Como has acertado, el turno sigue siendo tuyo                    
                    turno_jugador = True
#Si en esas coord ya hay una 'X' se indica que ya se había disparado y sigues disparando               
                elif tablero_maq[disparo_mio_x, disparo_mio_y] == "X":
                    print("Disparo previamente realizado por el jugador!")
                    print(tablero_visible)
                    print('\n')

                    turno_jugador = True
#Lo mismo si habías disparado pero había agua
                elif tablero_maq[disparo_mio_x, disparo_mio_y] == "-":
                    print("Disparo previamente realizado por el jugador!")
                    print('TABLERO VISIBLE')
                    print(tablero_visible)
                    print('\n')
                    time.sleep(1)
                    
                    turno_jugador = True
#Si en las coord dadas no hay nada en el tablero de la maq se pone un '-' y se modifican los tableros
#Se pierde el turno por lo que pasa a ser False
                elif tablero_maq[disparo_mio_x, disparo_mio_y] == " ":
                    tablero_maq[disparo_mio_x, disparo_mio_y] = "-"
                    tablero_visible[disparo_mio_x, disparo_mio_y] = '-'
                    print("AGUA!")
                    print(tablero_visible)
                    print('\n')
                    turno_jugador = False
                    continue

            else:
                print('HAS PERDIDO!')
                break
#Una vez el turno deje de ser tuyo, pasa a ser el de la máquina.
        if turno_jugador == False:
#Si hay barcos colocados en tu tablero, la maq dispara de manera aleatoria.           
            if 'O' in tablero_mine:
                disparo_maquina_x = np.random.randint(0,10)
                disparo_maquina_y = np.random.randint(0,10)
                
#El mismo código que en el caso anterior se repite y sigue el turno de la máq por acertar
                if tablero_mine[disparo_maquina_x, disparo_maquina_y] == "O":
                    tablero_mine[disparo_maquina_x, disparo_maquina_y] = "X"
                    print("LA MÁQUINA LO HA TOCADO!")
                    print(tablero_mine)
                    print('\n')
                    turno_jugador = False

                elif tablero_mine[disparo_maquina_x, disparo_maquina_y] == " ":
                    tablero_mine[disparo_maquina_x, disparo_maquina_y] = "-"
                    print("LA MÁQUINA HA DISPARADO AL AGUA!")
                    print(tablero_mine)
                    print('\n')
                    turno_jugador = True
                    
                elif tablero_mine[disparo_maquina_x, disparo_maquina_y] == "X":
                    print("Ese disparo ya se ha realizado previamente")
                    print(tablero_mine)
                    print('\n')
                    turno_jugador = False

                elif tablero_mine[disparo_maquina_x, disparo_maquina_y] == "-":
                    print("Ese disparo ya se ha realizado previamente")
                    print(tablero_mine)
                    print('\n')
                    time.sleep(1)
                    turno_jugador = False

            else:
                print('HAS GANADO!')
                break