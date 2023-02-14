from dataclasses import dataclass

def get_person(nombre, apellidos, edad):
    return {"nombre": nombre, "apellidos":apellidos, "edad": edad}

person = get_person("Bob", "Sponga", 4)
print(f"Person: {person['nombre']} {person['apellidos']}")

#class Person():
#   def __init__(self, nombre, apellidos, edad):
#       self.nombre = nombre
#       self.apellidos = apellidos
#       self.edad = edad

@dataclass
class Person:
    nombre: str
    apellidos: str
    edad: int

    def identify(self):
        return f"Person: {self.nombre} {self.apellidos}"

person2 = Person("Patricio", "Estrella Del Mar", 4)
print(f"Person: {person2.nombre} {person2.apellidos}")
print(person2.identify())



