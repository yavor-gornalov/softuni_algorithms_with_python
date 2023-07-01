# https://judge.softuni.org/Contests/Practice/Index/3465#3

from collections import deque


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


def find_path(node, parent):
    current_path = deque()
    while parent[node] is not None:
        current_path.appendleft(node)
        node = parent[node]
    return current_path


nodes_count = int(input())
edges_count = int(input())

graph = []
for _ in range(edges_count):
    source, destination, weight = [int(x) for x in input().split()]
    graph.append(Edge(source, destination, weight))

start_node = int(input())
end_node = int(input())

distance = [float("inf")] * (nodes_count + 1)
distance[start_node] = 0
parent = [None] * (nodes_count + 1)

for _ in range(nodes_count - 1):
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
        print("Undefined")
        break
else:
    path = deque()
    node = end_node

    while node is not None:
        path.appendleft(node)
        node = parent[node]

    print(*path, sep=" ")
    print(distance[end_node])
