import networkx as nx
import matplotlib.pyplot as plt
import random

def busqueda_profundidad(Grafo, inicio, destino, visited=None):
    # Si visited es None, inicializamos una lista vacía
    if visited is None:
        visited = []

    # Agregamos el nodo actual a la lista de visitados
    visited.append(inicio)

    # Si el nodo actual es el destino, devolvemos la lista de visitados
    if inicio == destino:
        return visited

    # Para cada nodo adyacente al nodo actual que no ha sido visitado, hacemos una llamada recursiva
    for next_node in Grafo[inicio]:
        if next_node not in visited:
            ruta = busqueda_profundidad(Grafo, next_node, destino, visited)
            if ruta is not None:
                return ruta

    # Si no se encontró una ruta al destino, devolvemos None
    return None


# Creamos un grafo aleatorio con 10 nodos y 15 aristas
G = nx.gnm_random_graph(10, 15)

# Asignamos pesos aleatorios entre 1 y 10 a cada arista
for u, v in G.edges():
    G.edges[u, v]['weight'] = random.randint(1, 10)

# Mostramos el grafo utilizando matplotlib
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()

# Ejecutamos el algoritmo de Búsqueda en Profundidad desde el nodo 0 al nodo 9
inicio = int(input("¿Cual es el nodo de origen (del 0 al 9)? "))
destino = int(input("¿Cual es el nodo de destino? "))
ruta = busqueda_profundidad(G, inicio, destino)
if ruta:
    print(f"La ruta desde el nodo {inicio} al nodo {destino} es: {ruta}")
else:
    print(f"No se pudo encontrar una ruta desde el nodo {inicio} al nodo {destino}")

# Creamos un subgrafo que contenga todos los nodos y aristas visitados durante la búsqueda en profundidad
grafo_resultado = G.subgraph(ruta)

# Mostramos el grafo resultado
nx.draw(grafo_resultado, nx.spring_layout(grafo_resultado), with_labels=True)
plt.show()
