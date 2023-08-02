# https://judge.softuni.org/Contests/Practice/Index/3464#2
"""
Bellman-Ford Algorithm
    Computes shortest paths from a source vertex to
    all the other vertices in a weighted digraph
    Can detect and report negative cycles

for v in G
    d[v] = infinity
    prev[v] = null
d[source] = 0
for vertex in G.vertices – 1
    for edge in edges
        if (d[edge.from] != infinity and
            d[edge.from] + edge.weight < d[edge.to])
        update d[edge.to]

Run the algorithm second time if you can
update any distance there is a negative cycle
"""

from collections import deque


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


def construct_graph(edges):
    graph = []  # Bellman-Ford algorithm needs only edges

    for _ in range(edges):
        source, destination, weight = [int(x) for x in input().split()]
        graph.append(Edge(source, destination, weight))

    return graph


def bellman_ford(start, graph):
    distance = [float("inf")] * (edges + 1)
    distance[start] = 0
    parent = [None] * (edges + 1)

    for _ in range(nodes - 1):
        updated = False
        for edge in graph:
            if distance[edge.source] == float("inf"):
                continue
            new_distance = distance[edge.source] + edge.weight
            if new_distance < distance[edge.destination]:
                distance[edge.destination] = new_distance
                parent[edge.destination] = edge.source
                updated = True
        if not updated:
            break

    for edge in graph:
        new_distance = distance[edge.source] + edge.weight
        if new_distance < distance[edge.destination]:
            raise Exception("Negative Cycle Detected")

    return distance, parent


def reconstruct_path(target, distance, parent):
    path = deque()
    node = target

    while node is not None:
        path.appendleft(node)
        node = parent[node]

    return path, distance[target]


nodes = int(input())
edges = int(input())
graph = construct_graph(edges)

start_node = int(input())
end_node = int(input())
try:
    distance, parent = bellman_ford(start_node, graph)
    path, path_distance = reconstruct_path(end_node, distance, parent)
    print(f"{' '.join([str(x) for x in path])}\n{path_distance}")
except Exception as err:
    print(*err.args)
