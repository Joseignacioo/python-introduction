#====== EXEPCIONES ======#
n1 = 5
n2 = 1
n3 = "1"

#====== TRY EXCEPT ======#
try:
    print(n1 + n2) 
    print("No se ha producido error")
except: # SE EJECUTA SI SE PRODUCE UNA EXCEPCION
    print("Se ha producido error") 

#====== TRY EXCEPT ELSE ======# OPCIONAL
try:
    print(n1 + n3) 
    print("No se ha producido error")
except:
    print("Se ha producido error")
else: # SE EJECUTA SI NO SE PRODUCE UNA EXCEPCION
    print("La ejecucion continua correctamente")

#====== TRY EXCEPT ELSE FINALLY ======# OPCIONAL
try:
    print(n1 + n2) 
    print("No se ha producido error")
except:
    print("Se ha producido error")
else:
    print("La ejecucion continua correctamente")
finally: # SE  EJECUTA SIEMPRE
    print("La ejecucion continua")

#====== EXCEPCIONES POR TIPO ERROR ======#
try:
    print(n1 + n3) 
    print("No se ha producido error") 
except TypeError: # SE EJECUTA SI SE PRODUCE UNA EXCEPCION
    print("Se ha producido TypeError") 

#====== CAPTURA DE LA INFORMACION DE LA EXCEPCION ======#
try:
    print(n1 + n3) 
    print("No se ha producido error")
except ValueError as error: # VARIABLE CAPTURANDO ERROR
    print(error)
except Exception as ExceptionError:
    print(ExceptionError)
 