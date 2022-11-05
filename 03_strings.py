#====== STRINGS ======#

a = "Mi String"
b = "Mi segundo String"
print(len(a))
print(len(b))
print(a + " " + b)

c = "Este es un String\ncon salto de linea"
print(c)

d = "\tEste es un String con tabulacion"
print(d)

e = "\\tEste es un String \\n escapado"
print(e)

#====== FORMATEO ======#
name, surname, age = "Jose", "Romero", 20
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) 
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) # $s = STRING, %d = ENTERO. ES MAS SEGURO
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

#====== DESEMPAQUEADO DE CARACTERES ======#
lenguaje = "python"
a, b, c, d, e, f = lenguaje
print(a)
print(e)

#====== DIVISION ======#
lenguaje_slice = lenguaje[1:3] # EL RANGO DEL 2 HASTA EL 3
print(lenguaje_slice)
lenguaje_slice = lenguaje[1:] #TODD MENOS EL PRIMERO
print(lenguaje_slice)
lenguaje_slice = lenguaje[-3] # DE DERECHA A IZQUIERDA
print(lenguaje_slice)
lenguaje_slice = lenguaje[1:2:4] #CARACTERES QUE NO SE VAN A MOSTRAR
print(lenguaje_slice)

#====== REVERSA ======#
lenguaje_reversa = lenguaje[::-1] # SE INVIERTE EL STRING
print(lenguaje_reversa)

#====== FUNCIONES ======#
print(lenguaje.count("t")) # CONTAR
print(lenguaje.capitalize()) # LA PRIMERA ENMAYUSCULA 
print(lenguaje.upper()) # TODD EN MAYUSCULA
print(lenguaje.lower()) # TODD MINUSCULAS
print(lenguaje.upper().isupper()) # TODD EN MAYUSCULAS, ¿ESTAN EN MAYUSCULAS?
print(lenguaje.isnumeric()) # ¿ES UN NUMERO?
print("1".isnumeric()) # ¿ES UN NUMERO?




