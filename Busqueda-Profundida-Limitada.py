"""
La principal diferencia entre la búsqueda en profundidad y la 
búsqueda en profundidad limitada es que en la búsqueda en profundidad 
limitada se establece un límite en la profundidad de búsqueda. Es decir, 
en lugar de explorar todos los nodos adyacentes de un nodo en una 
iteración, como lo hace la búsqueda en profundidad, la búsqueda en profundidad 
limitada solo explora los nodos adyacentes de un nodo hasta cierta profundidad 
dada por el límite establecido.

Si el nodo destino no se encuentra dentro del límite de profundidad establecido,
la búsqueda se detiene sin explorar otros nodos a mayor profundidad. Esto puede 
ser útil cuando se busca una solución en un espacio de búsqueda grande y se 
quiere evitar explorar caminos poco probables o de gran profundidad. Sin embargo, 
también puede llevar a no encontrar una solución óptima si esta se encuentra a una 
profundidad mayor que la establecida en el límite.
"""
import networkx as nx
import matplotlib.pyplot as plt
import random

#a la funcion le padamos el grafo, el nodo de inicio, el destino, el limite de profundidad
def busqueda_profundidad_limitada(Grafo, inicio, destino, limite, visited=None):
    # Si visited es None, inicializamos una lista vacía
    if visited is None:
        visited = []

    # Agregamos el nodo actual a la lista de visitados
    visited.append(inicio)

    # Si el nodo actual es el destino, devolvemos la lista de visitados
    if inicio == destino:
        return visited

    # Si se alcanzó el límite de profundidad, devolvemos None
    if limite == 0:
        return None

    # Para cada nodo adyacente al nodo actual que no ha sido visitado, hacemos una llamada recursiva
    for next_node in Grafo[inicio]:
        if next_node not in visited:
            ruta = busqueda_profundidad_limitada(Grafo, next_node, destino, limite-1, visited)
            if ruta is not None:
                return ruta

    # Si no se encontró una ruta al destino, devolvemos None
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

# Ejecutamos el algoritmo de Búsqueda en Profundidad Limitada desde el nodo 0 al nodo 9 con una profundidad máxima de 3
inicio = int(input("¿Cual es el nodo de origen? "))
destino = int(input("¿Cual es el nodo de destino? "))
profundidad = int(input("¿Cual es la profundidad máxima permitida? "))
ruta = busqueda_profundidad_limitada(G, inicio, destino, profundidad)
if ruta:
    print(f"La ruta desde el nodo {inicio} al nodo {destino} es: {ruta}")
    # Creamos un subgrafo que contenga todos los nodos y aristas visitados durante la búsqueda en profundidad limitada
    grafo_resultado = G.subgraph(ruta)

    # Mostramos el grafo resultado
    nx.draw(grafo_resultado, nx.spring_layout(grafo_resultado), with_labels=True)
    plt.show()

else:
    print(f"No se pudo encontrar una ruta desde el nodo {inicio} al nodo {destino}")

