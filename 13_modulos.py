#====== MODULOS ======#

#====== IMPORTAR TOD0 ======#
import modulos
modulos.print_name_2("Jose", "Romero")
modulos.funcion(5,2,1)

#====== DE MODULO IMPORTAR ALGO ======#
from modulos import print_name_2, funcion
print_name_2("Jose", "Romero")
funcion(5,2,1)

#====== ALGO DE LIBRERIA MATH ======#
import math
print(math.pi) # MOSTRAR PI
print(math.pow(2, 8)) #ELEVAR NUMEROS

#====== ALIAS O VARIABLE ======#
from math import pi as valor_pi
print(valor_pi)
