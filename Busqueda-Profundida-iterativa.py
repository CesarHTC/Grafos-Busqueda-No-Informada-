"""
La búsqueda en profundidad iterativa es una variante de la búsqueda en profundidad que
utiliza una estrategia iterativa para buscar en un árbol o grafo. La idea es ir aumentando
la profundidad de búsqueda de manera incremental en cada iteración hasta que se encuentre
el objetivo o se alcance el límite de profundidad.

Para implementar la búsqueda en profundidad iterativa, necesitamos una función auxiliar
que realice la búsqueda en profundidad a una profundidad máxima dada. Luego, en la función
principal, utilizamos un bucle para incrementar la profundidad de búsqueda y llamar a la
función auxiliar hasta que se encuentre el objetivo o se alcance el límite de profundidad.

La búsqueda en profundidad iterativa es más eficiente que la búsqueda en profundidad normal
en términos de tiempo y espacio ya que solo mantiene en memoria un camino a la vez y no tiene
que almacenar todos los caminos como lo hace la búsqueda en profundidad normal.
"""
import networkx as nx
import matplotlib.pyplot as plt
import random

def busqueda_profundidad_iterativa(Grafo, inicio, destino, profundidad_maxima):
    for profundidad in range(profundidad_maxima + 1):
        ruta = busqueda_profundidad_limitada(Grafo, inicio, destino, profundidad)
        if ruta:
            return ruta
    return None

#a la funcion le pasamos el grafo, el nodo de inicio, el destino, la profundidad maxima permitida
def busqueda_profundidad_limitada(Grafo, inicio, destino, profundidad_maxima, visited=None):
    if visited is None:
        visited = []
    visited.append(inicio)
    if inicio == destino:
        return visited
    if profundidad_maxima == 0:
        return None
    for next_node in Grafo[inicio]:
        if next_node not in visited:
            ruta = busqueda_profundidad_limitada(Grafo, next_node, destino, profundidad_maxima - 1, visited)
            if ruta is not None:
                return ruta
    return None

# Generamos un árbol balanceado con altura h y cada nodo interior tiene k hijos.
# Este tipo de árboles son árboles de ramificación completa.
#G = nx.balanced_tree(Hijos, Profundida)
G = nx.balanced_tree(2, 3)

# Asignamos pesos aleatorios entre 1 y 10 a cada arista
for u, v in G.edges():
    G.edges[u, v]['weight'] = random.randint(5, 18)

# Mostramos el grafo utilizando matplotlib
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()

# Ejecutamos el algoritmo de Búsqueda en Profundidad Iterativa desde el nodo 0 al nodo 9 con una profundidad máxima de 3
inicio = int(input("¿Cual es el nodo de origen? "))
destino = int(input("¿Cual es el nodo de destino? "))
profundidad_maxima = int(input("¿Cual es la profundidad máxima permitida? "))
ruta = busqueda_profundidad_iterativa(G, inicio, destino, profundidad_maxima)
if ruta:
    print(f"La ruta desde el nodo {inicio} al nodo {destino} es: {ruta}")
    # Creamos un subgrafo que contenga todos los nodos y aristas visitados durante la búsqueda en profundidad limitada
    grafo_resultado = G.subgraph(ruta)

    # Mostramos el grafo resultado
    nx.draw(grafo_resultado, nx.spring_layout(grafo_resultado), with_labels=True)
    plt.show()

else:
    print(f"No se pudo encontrar una ruta desde el nodo {inicio} al nodo {destino}")
