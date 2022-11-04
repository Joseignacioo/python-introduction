#VARIABLES TIPO 
variable_str = "Mi string Variable"
variable_int = 898
variable_boolean = False
print(variable_str, variable_int, variable_boolean)

# VARIABLES EN UNA LINEA + CONCATENACIÓN
name,  surname, alias, age = "Jose", "Romero", "Joseignacioo", 20
print(f"mi nombre es {name} {surname}, tengo {age} y mi alias es {alias}" ) #  f = .format

#FUNCIONES DEL SISTEMA
print(len(variable_str)) # len = contar caracteres "Mi string Variable"= (18)

# INPUT
name = input('Cual es  tu nombre?: ')
age = input('Cual es tu edad?: ')
print(f"Mi nombre es {name} y tengo {age}.")

