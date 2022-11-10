#====== LISTAS======#

tipo_lista = list([15, 23, "Juan", 2.0]) # TIPO DE LISTA
lista = [20, 1.67,"Jose", "Romero"] # [0, ,1, 2, 3,] o [-4, -3, -2, -1]

print(lista) 
print(len(lista)) # CONTAR LARGO DE LA LISTA
print(type(lista)) # TIPO DE DATO

print(lista[0]) # BUSCAR LA POSICION 0
print(lista[1]) # BUSCAR LA POSICION 1
print(lista[-1]) # BUSCAR LA POSICION -1

print(lista.count(20)) # CONTAR CUANTOS 20 HAY

age, height, name, surname = lista #VARIABLES CON ORDEN DE LISTA
print(name)
print(lista + tipo_lista) # UNIR LISTAS

lista.append("Quezada") # AGREGAR A LA LISTA
print(lista)

lista.insert(1, "Verde") # INSERTAR EN LA POSICION o  INDICE
print(lista)

lista[1] = "Rojo" # REMPLAZA EL VALOR DE LA POSICION o  INDICE
print(lista)

lista.remove("Rojo") # ELIMINAR EL VALOR INDICADO
print(lista)

# ELIMINA EL ULTIMO DE LA LISTA
print(lista.pop()) # ME RETORNA EL VALOR ELIMINADO 
print(lista.pop(2)) # ELIMINAR EN LA POSICION o  INDICE
print(lista)

del lista[2] # ELIMINAR EN LA POSICION o  INDICE
print(lista)

nueva_lista = lista.copy() # COPIAR LISTA

lista.clear() # BORRAR LA LISTA 
print(lista)
print(nueva_lista) # NO SE BORRA ESTA LISTA

nueva_lista.reverse() # ORDENA LOS VALORES ALREVES
print(nueva_lista) 

nueva_lista.sort() # ORDEN ALFABETICO O DE MENOR A MAYOR
print(nueva_lista)

print(nueva_lista[1:2]) # SUBLISTAS

