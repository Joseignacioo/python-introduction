#====== SETS ======#

tipo_set = set()
sets = {}

print(type(tipo_set)) 
print(type(sets)) # INICIALMENTE ES UN DICCIONARIO

sets = {"Jose", "Romero", 20}
print(type(sets)) # AHORA LO TRANSFORMA EN SET
print(len(sets))

sets.add(1.68) #AGREGA PERO UN SET NO  ES UNA ESTRUCTURA ORDENADA
print(sets)

sets.add(1.68) # UN SET NO AGREGA REPETIDOS
print(sets)

print("Jose" in sets) #EXISTE EN EL SET ? 
print("Quezada" in sets) #EXISTE EN EL SET ? 

sets.remove(1.68) #ELIMINAR EL VALOR INDICADO
print(sets)

sets.clear() # BORRA TODOS LOS ELEMENTOS DEL SET
print(len(sets))

sets = {"Jose", "Romero", 20}
otro_sets = {"python", "javascript", "java"} # UNIR SETS
new_set = sets.union(otro_sets)
print(new_set)

del sets # ELIMINA INCLUYENDO EL SET
print(sets)


