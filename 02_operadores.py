#====== OPERADORES ======#

print(15+2) # SUMA
print(15-2) # RESTA
print(15*2) # MULTIPLICACION
print(15/2) # DIVISION
print(15%2) # RESTO
print(15//2) # DIVISION APROXIMADA A NUMERO ENTERO
print(15**2) # EXPONENTE

print("Hola " + "Python") # CONCATENACION CON (+)
print("Hola " + str(5))  # TRANSFORMAR UN (INT) EN (STRING) CON STR()
print("Hola " * 5) # MULTIPLICAR LA PALABRA 5 VECES
print("Hola " * (2**3)) #MULTIPLICA LA PALABRA 2**3 = 8 VECES

variable_float = 2.5 * 2 
print("Hola " * int(variable_float)) # TRANSFORMAR UN (FLOAT) EN (ENTERO) CON INT()

#====== OPERADORES COMPARATIVOS ======#
print(3 > 4) # MAYOR A
print(3 < 4) # MENOR A
print(3 >= 4) # MAYOR IGUAL A
print(3 <= 4) # MENOR IGUAL A
print(3 == 4) # IGUALDAD A
print(3 != 4) # DISTINTO A

print("Hola " > "Python")
print("Hola " < "Python")
print("Hola " >= "Python")
print("Hola " <= "Python")
print("Hola " == "Python")
print("Hola " != "Python")

#====== OPERADORES LOGICOS ======#
print(3 > 4 and "Hola " > "Python") # FALSE and FALSE = FALSE
print(3 > 4 or "Hola " > "Python") # FALSE or FALSE = FALSE
print(3 < 4 and "Hola " > "Python") # TRUE and TRUE = FALSE
print(3 < 4 or "Hola " > "Python") # TRUE or FALSE = TRUE
print(not(3 > 4)) # NOT = NEGAR LA CONDICION 

