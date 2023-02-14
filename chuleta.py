from dataclasses import dataclass

def person(nombre, appelidos, edad):
    return {"nombre": nombre, "appelidos":appelidos, "edad": edad}

person = person("Patricio", "Estrella Del Mar", 4)
print(f"Person: {person['nombre']} {person['appelidos']}")

#class Person():
#   def __init__(self, nombre, appelidos, edad):
#       self.nombre = nombre
#       self.appelidos = appelidos
#       self.edad = edad

@dataclass
class Person:
    nombre: str
    appelidos: str
    edad: int

    def identify(self):
        return f"Person: {person.nombre} {person.appelidos}"

person2 = Person("Patricio", "Estrella Del Mar", 4)
print(f"Person: {person2.nombre} {person2.appelidos}")
print(person2.identify())



