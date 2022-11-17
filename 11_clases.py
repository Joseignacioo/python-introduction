#====== CLASES ======#

class TipoClase: # CARNEL CASE
    pass # EJECUTAR EL PROGRAMA SIN CAUSAR ERROR

print(TipoClase)
print(TipoClase())

#====== CLASES CON PARAMETROS ======#
class Persona_1:
    def __init__(self, name, surname):  # CREAR CONSTRUCTOR DE CLASE, NO ES UNA FUNCION
        self.name = name
        self.surname = surname 
        
person = Persona_1("Jose", "Quezada")
print(f"{person.name} {person.surname}")


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

