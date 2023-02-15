from dataclasses import dataclass
import webbrowser
import time

def get_person(nombre, apellidos, edad):
    return {"nombre": nombre, "apellidos":apellidos, "edad": edad}

def print_person(pers):
    print(f"Person: {pers['nombre']} {pers['apellidos']}")

def show_message(pers):
    if pers['nombre'] == 'Bob'and pers['apellidos'] == 'Sponga': 
        print("""¿Estáis listos chicos?
¡Sííí capitán!
Más fuerteee..
¡Sííí capitán!
uuuhhhh….
Él vive en la piña debajo del mar
¡Bob Esponja!
Su cuerpo amarillo absorbe sin más
Bob Esponja!)""") 
    else:
        print("Tu no eres Bob Sponga!")

bob = {'nombre': 'Bob', 'apellidos': 'Sponga',  "edad": 4}
patricio = get_person("Patricio", "Estrella", 3)

print(f"Person: {bob['nombre']} {bob['apellidos']} (edad: {bob['edad']})")
show_message(bob)

print_person(patricio)

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
        return f"Person: {self.nombre} {self.apellidos} (edad: {self.edad})"
    
    def show_me(self):
        webbrowser.open_new_tab(f"https://www.google.com/search?q={self.nombre}+{self.apellidos}")

calamar = Person("Calamardo", "Tentáculus", 5)

print(calamar.identify())
calamar.show_me()

#On Windows we need to wait a bit to have the action completed
time.sleep(1)


