#====== TUPLAS ======#
tipo_tupla = tuple([15, 23, "Juan", 2.0])
tupla = (20, 1.67,"Jose", "Romero")

print(tupla)
print(len(tupla))
print(type(tupla))

print(tupla[0]) # BUSCAR LA POSICION 0
print(tupla[1]) # BUSCAR LA POSICION 1
print(tupla[-1]) # BUSCAR LA POSICION -1

print(tupla.count(20))  # CONTAR CUANTOS 20 HAY
print(tupla.index("Jose")) # NOS MUESTRA LA  POSICION o INDICE DEL ELEMENTO

print(tupla[2:6]) #subtupla

print(tipo_tupla + tupla) # UNIR TUPLAS

tupla = list(tupla) # TRANSFORMAR LA  TUPLA  EN LISTA
print(type(tupla))

#CUANDO LO TRANSFORMAMOS A LISTA Y MODIFICAR
tupla[3] = "Quezada" #  REMPLAZAR  POR POSICION O INIDCE
tupla.insert(1, "Verde") #INSERTAR 

tupla = tuple(tupla) #TRANSFORMAR LA LISTA EN TUPLA
print(tupla) 
print(type(tupla))

age, color, *resto = tupla
print(age)
print(color)
print(resto) # RETORNAR EL RESTO EN LISTA

age, color, *_, surname = tupla
print(age)
print(color)
print(surname) # OMITE LOS DATOS

# ZIP
lista = [1,2,3,4,5]
nueva_tupla = (10.20,30,40,50)
lista_2 = [100,200,300,400,500]
resultado = zip(lista,nueva_tupla,lista_2) #ZIP
resultado = tuple(resultado)
print(resultado)

del tupla # ELIMINA TODA LA TUPLA
