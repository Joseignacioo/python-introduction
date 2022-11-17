#====== LOOPS/BUCLES/CICLOS ======#

#====== WHILE ======# cumplir una condicion
condicion = 0
while condicion < 10: # REPITE  INFINITAS  VECES LA CONDICION HASTA QUE SEA FALSE
    print(condicion)
    condicion += 1 # TERMINA LA EJECUCION CUANDO LLEGUE A 10
else: # EJECUTA JUSTO CUANDO SE  CUMPLE EL WHILE
    print("Mi condicion es mayor o igual que 10")


while condicion < 20:
    condicion += 1
    if condicion == 15:
        print("Se detiene la ejecucion")
        break # TERMINAR EL PROCESO
    print("Mi condicion es  menor a 20")

#====== FOR ======# ver cuantos elementos le indicamos de una posible iteracion o lista
lista = [35, 24, 62, 52, 30, 30, 17]
for elemento in lista:
    print(elemento)

tupla = (20, 1.67,"Jose", "Romero")
for elemento in tupla:
    print(elemento)

sets = {"Jose", "Romero", 20}
for elemento in sets:
    print(elemento)

diccionario = {"Nombre":"jose", "Apellido":"Romero", "edad":20,"lenguajes":{"python", "javascript"}}
# for elemento in diccionario.values():
for elemento in diccionario:
    print(elemento)
    if elemento == "edad":
        # break
        continue # SE SALTA LA  EJECUCION Y PASA A LA SIGUIENTE
    print("Se ejecuta")
else:
    print("El  bucle for para diccionario termino")


#====== FOR IN RANGE======#
for i in range(10):
    print(i)

for i in range(15,20):
    print(i)

for i in range(1,10,2):
    print(i)

#====== FOR IN ENUMERATE======#
numeros = [10, 20, 30, 40, 50]
for i, numero in enumerate(numeros):
    i += 1 
    print(f'{i}) {numero}')