#====== CLASES ======#

class TipoClase: # CARNEL CASE
    pass # EJECUTAR EL PROGRAMA SIN CAUSAR ERROR

print(TipoClase)
print(TipoClase())

#====== ATRIBUTOS DE CLASES ======#
class Usuario:
    username = 'Username por default'
    email = ''
Usuario.username = 'User1'
Usuario.email = 'jost.jeje@gmail.com'
print(Usuario.username)
print(Usuario.email)

#====== ATRIBUTOS DE INSTACIA ======#
class Usuario1:
    username = 'Username por default'
    email = ''
user1 = Usuario1()
# 1- VERIFICA SI EL ATTR EXISTE DENTRO DEL OBJECTO
# 2- VERIFICA SI EL ATTR EXISTE DENTRO DE LA CLASE -> LECTURA
# 3- LANZAR UN ERROR
user1.username = 'Joseignacioo' # AÑADIR ATRIBUTOS AL OBJETO
user1.password = '1234'
print(user1.username)

print(id(user1.username))
print(id(Usuario1.username))

print(user1.__dict__) # DICCIONARIO

#====== CLASES CON PARAMETROS ======#
class Persona_1:
    def __init__(self, name, surname):  # CREAR CONSTRUCTOR DE CLASE, NO ES UNA FUNCION
        self.name = name
        self.surname = surname 
        
person = Persona_1("Jose", "Quezada")
print(f"{person.name} {person.surname}")

print(person.__dict__)

class Persona_2:
    def __init__(self, name, surname, alias = "Sin Alias"):  # CREAR CONSTRUCTOR DE CLASE, NO ES UNA FUNCION
        self.full_name = f"{name} {surname} ({alias})"

    def caminar(self):
        print(f"{self.full_name} Esta caminando")

person_1 = Persona_2("Jose", "Romero")
print(person_1.full_name)
person_1.caminar()

person_2 = Persona_2("Jose", "Romero", "Joseignacioo")
print(person_2.full_name)
person_2.caminar()
person_2.full_name = "Hector de leon (El loco Perro)"
print(person_2.full_name)

print(person_1.__dict__)
print(person_2.__dict__)


#====== CLASES CON HERENCIA y HERENCIA MULTIPLES ======#
class Animal: #CLASE PADRE
    def comer(self):
        print('El animal come')
    def dormir(self):
        print('El animal duerme')

class Mascota(Animal): 
    def comer(self):
        print('La mascota  come')

class Felino: # CLASE HIJO
    def cazar(self):
        print('El felino caza')

class Gato(Mascota, Felino):
    def __init__(self, nombre):
        self.nombre = nombre
    def comer(self):
        super().comer() # ACCEDE AL LA CLASE  PADRE  PARA USAR SUS METODOS
        print(f'{self.nombre}  come')
    def dormir(self):
        print(f'{self.nombre} duerme')

patricio = Gato('Patricio')
patricio.comer()
patricio.dormir()

#====== METODOS  DE CLASE ======#
class Circulo:

    pi = 3.141592

    @classmethod
    def area(cls, radio):
        return cls.pi * (radio ** 2)
resultado= Circulo.area(14)
print(resultado)

a ='false' or () or []
print(a)