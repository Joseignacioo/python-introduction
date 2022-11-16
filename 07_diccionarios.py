#====== DICCIONARIO ======#

tipo_diccionario = dict()
diccionario = {}

print(type(tipo_diccionario))
print(type(diccionario))

diccionario = {
    "Nombre":"jose", 
    "Apellido":"Romero", 
    "edad":20,
    "lenguajes":{"python", "javascript"} 
    }

print(diccionario)
print(len(diccionario)) # SON KEY Y CONTENIDO

print(diccionario["Nombre"]) # RETORNAR EL VALOR INDICADO

diccionario["Nombre"] = "José" # REMPLAZAR DATOS
print(diccionario["Nombre"])

diccionario["Educacion"] = "Duoc UC" # AGREGAR DATOS 
print(diccionario)

del diccionario["Educacion"] # ELIMINAR EN LA POSICION o  INDICE
print(diccionario)

print("José" in diccionario) # EXISTE EN EL DICCIONARIO ? BUSCA POR KEYS
print("Apellido" in diccionario) #EXISTE EN EL DICCIONARIO ? 

print(diccionario.items()) # RETORNA EL DICCIONARIO DE ITEM UN LISTADO
print(diccionario.keys())  # SOLO RETORNA LAS KEYS
print(diccionario.values()) # SOLO RETORNA LOS VALORES

new_diccionario = dict.fromkeys(("Nombre", 1)) # PARA CREAR UN DICCIONARIO
print(new_diccionario)

