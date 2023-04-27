"""
La búsqueda bidireccional es un algoritmo de búsqueda en grafos que parte de dos 
nodos distintos (generalmente el nodo de origen y el nodo de destino) y se mueve 
hacia el centro del grafo. En lugar de expandir todo el grafo, este algoritmo }
explora desde dos puntos, uno en la dirección de inicio y otro en la dirección de 
destino, y se detiene cuando ambos encuentran un nodo en común.


La búsqueda bidireccional es una forma de reducir el espacio de búsqueda y la 
complejidad del algoritmo, en comparación con la búsqueda en profundidad o la 
búsqueda en anchura, ya que se exploran dos caminos a la vez, reduciendo el número 
de nodos explorados. En general, la búsqueda bidireccional suele ser más eficiente 
que la búsqueda unidireccional en grafos grandes y complejos.

"""

##################################
import networkx as nx
import matplotlib.pyplot as plt
import random

def busqueda_bidireccional(Grafo, inicio, destino):
    visitados_inicio = {inicio: None}
    visitados_destino = {destino: None}

    while True:
        interseccion = set(visitados_inicio.keys()) & set(visitados_destino.keys())

        if interseccion:
            nodo_comun = interseccion.pop()
            ruta_inicio = obtener_ruta(visitados_inicio, nodo_comun)
            ruta_destino = obtener_ruta(visitados_destino, nodo_comun)
            ruta_destino.reverse()
            return ruta_inicio + ruta_destino

        nuevos_nodos_inicio = {}
        for nodo in visitados_inicio:
            for vecino in Grafo[nodo]:
                if vecino not in visitados_inicio and vecino not in nuevos_nodos_inicio:
                    nuevos_nodos_inicio[vecino] = nodo
        if not nuevos_nodos_inicio:
            return None
        visitados_inicio.update(nuevos_nodos_inicio)

        nuevos_nodos_destino = {}
        for nodo in visitados_destino:
            for vecino in Grafo[nodo]:
                if vecino not in visitados_destino and vecino not in nuevos_nodos_destino:
                    nuevos_nodos_destino[vecino] = nodo
        if not nuevos_nodos_destino:
            return None
        visitados_destino.update(nuevos_nodos_destino)

def obtener_ruta(visitados, nodo):
    ruta = [nodo]
    while visitados[nodo] is not None:
        nodo = visitados[nodo]
        ruta.append(nodo)
    ruta.reverse()
    return ruta

# Creamos un grafo aleatorio con 20 nodos y 40 conexiones
G = nx.gnm_random_graph(20, 30)

# Asignamos pesos aleatorios entre 10 y 10000 a cada conexion
for u, v in G.edges():
    G.edges[u, v]['weight'] = random.randint(10, 100)

# Mostramos el grafo utilizando matplotlib
pos = nx.spring_layout(G, k=0.2)
nx.draw(G, pos, with_labels=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
# Ejecutamos el algoritmo de Búsqueda Bidireccional desde el nodo 0 al nodo 9
inicio = int(input("¿Cual es el nodo de origen? "))
destino = int(input("¿Cual es el nodo de destino? "))
ruta = busqueda_bidireccional(G, inicio, destino)
if ruta:
    print(f"La ruta desde el nodo {inicio} al nodo {destino} es: {ruta}")
    # Creamos un subgrafo que contenga todos los nodos y aristas visitados durante la búsqueda
    grafo_resultado = G.subgraph(ruta)

    # Mostramos el grafo resultado
    nx.draw(grafo_resultado, nx.spring_layout(grafo_resultado), with_labels=True)
    plt.show()

else:
    print(f"No se pudo encontrar una ruta desde el nodo {inicio} al nodo {destino}")
