import networkx as nx
import itertools as it
import math
import matplotlib.pyplot as plt

G = nx.Graph()
cubes = list(it.product(range(3), repeat=3))
for i, cube in enumerate(cubes):
    G.add_node(i, cube=cube)
for i, cube in enumerate(cubes):
    for j, other_cube in enumerate(cubes):
        if sum((a - b) ** 2 for a, b in zip(cube, other_cube)) == 1:
            G.add_edge(i, j)


# show path from 1,1,1 to every vertex without repeating any vertex (minimum path)
for i, cube in enumerate(cubes):
    if cube == (1, 1, 1):
        start = i
        break


# hamiltonian path
# first, turn the graph into a directed graph
# then, find a hamiltonian path
# finally, draw the path
G = nx.DiGraph(G)
path = nx.tournament.hamiltonian_path(G)


nx.draw(G, with_labels=True)
plt.show()
