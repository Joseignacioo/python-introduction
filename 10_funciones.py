#====== FUNCIONES ======#

#====== FUNCION SIMPLE ======#
def funcion():
    # DOCUMENTAR LA FUNCION
    """
    La  funcion retorna  
    un string
    """
    print("Esto es una funcion")

funcion()
funcion()

#====== FUNCION CON PARAMETROS ======#
def sum_values_1(n1, n2): #PARAMETROS
    print(n1 + n2)

valor = 2
sum_values_1(valor, 2) # AGREGAR VALORES PARA EL PARAMETRO
sum_values_1("3", "9") # CONCATENA NUMEROS
sum_values_1(1.3, 2.2) # SUMAR CON FLOAT

#====== FUNCION CON PARAMETROS INT ======#
def sum_values_2(n1: int, n2: int): #PARAMETROS EXIGE QUE TENGA UN INT
    print(n1 + n2)

sum_values_2(2, 2) # AGREGAR VALORES PARA EL PARAMETRO


#====== FUNCION CON PARAMETROS RETURN ======#
def sum_values_3(n1, n2): #PARAMETROS
    return n1 + n2

resultado = sum_values_3(10, 5)
print(resultado)
print(sum_values_3(10, 5))

#====== FUNCION CON PARAMETROS ORDENAR ======#
def print_name_1(name, surname):
    print(f"{name} {surname}")

print_name_1(surname="Romero", name="Jose") # LLAMAR AL PARAMETRO PARA ORDENAR


#====== FUNCION CON PARAMETROS VALOR POR DEFECTO ======#
def print_name_2(name, surname, alias = "Sin alias"): # ALIAS = VALOR POR DEFECTO
    print(f"{name} {surname} {alias}")

print_name_2("Jose","Romero")
print_name_2("Jose","Romero","Joseignacioo")

#====== FUNCION CON PARAMETROS AGREGAR PARAMETROS ======#
def print_texts(*texts): # NUMERO  DE PARAMETROS DINAMICO tupla
    for text in texts:
        print(text.upper())
        print(type(texts))

print_texts("Hola", "Python", "Java") 

def usuarios(**kwargs): # NUMERO DE PARAMETROS DINAMICO diccionario
    print(kwargs)
    print(type(kwargs))

usuarios(Jose=[10, 10, 8], fernando=[10, 9, 9])

#====== FUNCION DENTRO DE OTRA FUNCION ======#
def operacion(cantidad, balance, tipo="deposito"):
    def deposito(cantidad, balance):
        return cantidad + balance

    def retiro(cantidad , balance):
        if cantidad <= balance:
            return  balance - cantidad
        else:
            return None

    if tipo == 'deposito':
        return deposito(cantidad, balance)
    elif tipo == 'retiro':
        return retiro(cantidad, balance)

resultado = operacion(10, 30)
print(resultado)
resultado = operacion(10, 30, 'retiro')
print(resultado)


#====== GENERADOR ======#
def pares():
    for n in range(0, 100, 2):
        yield n # LA  FUNCION SUSPENDE EJECUCION
        print("Se renuda la ejecucion")

for i in pares():
    print(i)


