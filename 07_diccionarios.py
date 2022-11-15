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