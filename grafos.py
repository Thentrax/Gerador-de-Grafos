import igraph as ig
from igraph import plot

def graph_plot(graph, x_box, y_box, color, layout_type):   
    # Instância Graph
    grafo = ig.Graph()

    # Separando chaves do dicionário
    graph_keys = list(graph.keys())

    # Adicionando n vértices no grafo
    grafo.add_vertices(len(graph_keys))

    # Encontrando índices das arestas e as adicionando no grafo
    graph_edges = []

    for i, key in enumerate(graph_keys):
        for j in graph[key]:
            if not (graph_keys.index(j), i) in graph_edges:
                graph_edges.append((i, graph_keys.index(j)))

    grafo.add_edges(graph_edges)

    # Plotagem do grafo
    box = (x_box, y_box)
    layout = Grafo.layout(layout_type) # circle, drl, fr, kk, large, random, rt, rt_circular
    cores = [color] * len(graph_keys)
    return plot(Grafo, layout=layout, bbox = box, vertex_label=graph_keys, vertex_color=cores)

