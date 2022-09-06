from Grafos import graph_plot

print('''A''')

# graph = {'A': ['B', 'C', 'F'],
#                  'B': ['A', 'C'],
#                  'C': ['A', 'B', 'D'],
#                  'D': ['C'],
#                  'E': [],
#                  'F': ['A']}

graph = {'1': ['2', '4'],
         '2': ['1', '3'],
         '3': ['2'],
         '4': ['1'],
         '5': []}





graph_plot(graph, 300, 300, 'white', 'circle')