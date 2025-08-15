from collections import deque

class Persona:
    def __init__(self, codigo, nombre, telefono:int, edad:int):
        self.codigo = codigo
        self.nombre = nombre
        self.telefono = telefono
        self.edad = edad
