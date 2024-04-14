import funciones as fun
import variables as var
#importo las funciones y las variables

#Con las primeras tres funciones creo los tableros vacíos
fun.init_tablero_mine(fill=' ')

fun.init_tablero_maq(fill=' ')

fun.init_tablero_visible(fill='?')

#Después agrego los barcos
fun.generar_todos_los_barcos_mios()
#Y también lo hace la maq
fun.generar_todos_los_barcos_maquina()

#Por último se le llama a la función de disparar.
fun.disparar(var.tablero_mine,var.tablero_maq,var.tablero_visible)


