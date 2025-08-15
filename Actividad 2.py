from collections import deque

class Persona:
    def __init__(self, codigo:int, nombre, telefono:int, edad:int):
        self.codigo = codigo
        self.nombre = nombre
        self.telefono = telefono
        self.edad = edad

    def __str__(self):
        return (f"{self.codigo}, {self.nombre}. {self.telefono}, {self.edad}")

def ingresoPersonas():
    listaPersonas= deque()
    print("--Ingreso de personas--")
    while True:
        try:
            codigo=int(input("Ingrese el codigo de la persona: "))
            nombre=input("Ingrese el nombre de la persona: ")
            telefono=int(input("Ingrese el telefono de la persona: "))
            edad=int(input("Ingrese la edad de la persona: "))
            persona= Persona(codigo, nombre, telefono, edad)

            listaPersonas.append(persona)
            otraPersona=input("Desea continuar? SI-NO: ").upper()

            if otraPersona!="SI":
                break

        except ValueError:
            print("Ingrese un valor valido")

    return listaPersonas

def salidaPersonas(listaPersonas):
    print("--Listado de personas--")
    for persona in listaPersonas:
        print(persona)

personas=ingresoPersonas()
salidaPersonas(personas)
