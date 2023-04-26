import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Arbol:
    def __init__(self, elemento):
        self.hijos = []
        self.elemento = elemento

def buscarSubarbol(arbol, elemento):
    if arbol.elemento == elemento:
        return arbol
    for subarbol in arbol.hijos:
        arbolBuscado = buscarSubarbol(subarbol, elemento)
        if (arbolBuscado != None):
            return arbolBuscado
    return None         

def agregarElemento(arbol, elemento, elementoPadre):
    subarbol = buscarSubarbol(arbol, elementoPadre);
    subarbol.hijos.append(Arbol(elemento))


def profundidad(arbol):
    if len(arbol.hijos) == 0: 
        return 1
    return 1 + max(map(profundidad,arbol.hijos)) 
def grado(arbol):
    return max(map(grado, arbol.hijos) + [len(arbol.hijos)])

abuelo = "A"
Rama_B = "B"
Rama_C = "C"
Rama_D = "D"
Hoja_B_E = "E"
Hoja_B_F = "F"
Hoja_D_G = "G"
Hoja_G_J = "J"
Hoja_D_H = "H"
Hoja_H_I = "I"
arbol = Arbol(abuelo)
agregarElemento(arbol, Rama_B, abuelo)
agregarElemento(arbol, Rama_C, abuelo)
agregarElemento(arbol, Rama_D, abuelo)
agregarElemento(arbol, Hoja_B_E, Rama_B)
agregarElemento(arbol, Hoja_B_F, Rama_B)
agregarElemento(arbol, Hoja_D_G, Rama_D)
agregarElemento(arbol,Hoja_G_J,Hoja_D_G)
agregarElemento(arbol, Hoja_D_H, Rama_D)
agregarElemento(arbol,Hoja_H_I,Hoja_D_H)

def ejecutarAnchoPrimero(arbol, funcion, cola = deque()):
    funcion(arbol.elemento)
    if (len(arbol.hijos) > 0):
        cola.extend(arbol.hijos)
    if (len(cola) != 0):
        ejecutarAnchoPrimero(cola.popleft(), funcion, cola)
          

def printElement(element):
    print(element)

ejecutarAnchoPrimero(arbol, printElement)

