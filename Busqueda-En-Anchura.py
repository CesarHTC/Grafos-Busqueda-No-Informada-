import networkx as nx
import matplotlib.pyplot as plt

# Definimos un diccionario para asignar colores a valores numéricos únicos
color_map = {'rojo': 1, 'azul': 2, 'verde': 3, 'amarillo': 4}

# Creamos el grafo
G = nx.Graph()

# Añadimos nodos al grafo con atributos adicionales
G.add_node(1, label="Nodo 1", color="rojo")
G.add_node(2, label="Nodo 2", color="azul")
G.add_node(3, label="Nodo 3", color="verde")
G.add_node(4, label="Nodo 4", color="rojo")
G.add_node(5, label="Nodo 5", color="amarillo")
G.add_node(6, label="Nodo 6", color="rojo")

# Añadimos aristas al grafo
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 5), (4, 6), (5, 6)])

# Imprimimos los nodos y las aristas
print("Nodos del grafo:")
for n in G.nodes:
    print(n, G.nodes[n])

print("Aristas del grafo:", G.edges)

# Realizamos la búsqueda en anchura
bfs_tree = nx.bfs_tree(G, 1)
print("Resultado de la búsqueda en anchura:", list(bfs_tree))

# Dibujamos el grafo
pos = nx.spring_layout(G)
node_colors = [color_map[G.nodes[n]['color']] for n in G.nodes]
nx.draw_networkx_nodes(G, pos, node_color=node_colors)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos, labels={n:G.nodes[n]['label'] for n in G.nodes})
nx.draw_networkx_edges(bfs_tree, pos, edge_color='r', alpha=0.5)

# Mostramos el grafo
plt.axis('off')
plt.show()
