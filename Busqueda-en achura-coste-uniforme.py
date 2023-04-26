import networkx as nx
import matplotlib.pyplot as plt
import random
import heapq

def Coste_uniforme(Grafo, inicio, destino):
    # Inicializamos la cola de prioridad con el nodo de inicio y su coste acumulado 0
    queue = [(0, inicio)]
    # Inicializamos un diccionario para llevar registro del coste acumulado de cada nodo
    cost_so_far = {inicio: 0}
    # Inicializamos un diccionario para llevar registro de la ruta tomada para llegar a cada nodo
    came_from = {inicio: None}

    while queue:
        # Sacamos el nodo con el menor coste acumulado de la cola de prioridad
        current_cost, current_node = heapq.heappop(queue)

        # Si llegamos al nodo objetivo, devolvemos la ruta tomada para llegar a él
        if current_node == destino:
            path = [current_node]
            while came_from[current_node] is not None:
                path.append(came_from[current_node])
                current_node = came_from[current_node]
            path.reverse()
            return path

        # Para cada vecino del nodo actual, calculamos el coste acumulado si tomamos la ruta actual
        for next_node in Grafo[current_node]:
            weight = Grafo.edges[current_node, next_node]['weight']
            new_cost = current_cost + weight

            # Si este vecino no ha sido visitado todavía o el nuevo coste acumulado es menor que el anterior, lo agregamos a la cola de prioridad
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost
                heapq.heappush(queue, (priority, next_node))
                came_from[next_node] = current_node

    # Si no se pudo llegar al nodo objetivo, devolvemos None
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

# Ejecutamos el algoritmo de Búsqueda de Coste Uniforme desde el nodo 0 al nodo 9
inicio = int(input("¿Cual es el nodo de origen(Del 0 al 9))?"))
destino = int(input("¿Cual es el nodo de destino?"))
Ruta = Coste_uniforme(G, inicio, destino)
if Ruta:
    print(f"La ruta más corta desde el nodo {inicio} al nodo {destino} es: {Ruta}")
else:
    print(f"No se pudo encontrar una ruta desde el nodo {inicio} al nodo {destino}")
#grafo resultado
Grafo = nx.Graph()
#Agregamos los nodos al grafo
for i in Ruta:
    Grafo.add_node(i)

for i in range (len(Ruta)):
    if i<(len(Ruta)-1):
        Grafo.add_edge(Ruta[i],Ruta[i+1])


    

nx.draw(Grafo, nx.spring_layout(Grafo), with_labels=True)    
plt.show()