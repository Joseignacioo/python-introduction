#====== CONDICIONALES ======#

condicional = True
if condicional:
    print("Se ejecuta correctamente")
if condicional == True:
    print("Se ejecuta correctamente") # ES LO MISMO QUE LA ANTERIOR

#====== ELSE  ======#
condicional = 5 * 2
if condicional == 10: # SI LA CONDICION CUMPLE  
    print("Se ejecuta la condicion 1")
if condicional > 10 and condicional < 20:
    print("Se ejecuta la condicion 2")
else:  # SI LA  CONDICION NO CUMPLE
    print("Es menor oo igual que 10 o mayor o igual que 20") 

#====== ELIF ======#
condicional = 7
if condicional == 10: # SI LA CONDICION CUMPLE  
    print("FELICIDADES APROVASTE TIENES UN 10")
elif condicional == 9 or condicional == 8:
    print("FELICIDADES APROVASTE")
elif condicional == 7 or condicional == 6:
    print("APROVASTE")
else:  # SI LA  CONDICION NO CUMPLE
    print("REPROVASTE") 

#====== NOT ======#
string = ""
if not string:
    print("Mi cadena de texto esta vacia")
if string == "Python":
    print("Coincide")


#====== TERNAEARIO ======#
calificacion = 10
color = 'verde' if calificacion >= 7 else 'rojo'
print(calificacion, color)