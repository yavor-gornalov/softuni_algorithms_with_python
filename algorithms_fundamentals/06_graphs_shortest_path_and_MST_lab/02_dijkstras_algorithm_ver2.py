# https://judge.softuni.org/Contests/Practice/Index/3464#1
"""
Dijkstra's algorithm finds the shortest path from given vertex to
all other vertices in a directed / undirected weighted graph
    Weights on edges are non-negative
    Edges can be directed or not
    Weights do not have to be distances
    Shortest path is not necessarily unique
    Not all edges need to be reachable

d[0…n-1] = INFINITY; d[startNode] = 0
Q = priority queue holding nodes ordered by distance d[]
startNode add to Q
while (Q is not empty)
    minNode = dequeue the smallest node from Q
    if (d[minNode] == INFINITY) break;
    foreach (child c of minNode)
        if (c is unvisited) c add to Q
        newDistance = d[minNode] + distance {minNode → c}
        if (newDistance < d[c])
            d[c] = newDistance;
            reorder Q;
"""

from collections import deque
from queue import PriorityQueue


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


def construct_graph(edges):
    graph = {}
    for _ in range(edges):
        source, destination, weight = [int(x) for x in input().split(", ")]
        if source not in graph:
            graph[source] = []
        if destination not in graph:
            graph[destination] = []
        edge = Edge(source, destination, weight)
        graph[source].append(edge)
        # graph[destination].append(edge) # for undirected graph
    return graph


def dijkstra(start, target, graph):
    max_node = max(graph.keys())  # for graph with integer nodes and not continuous numeration

    distance = [float("inf")] * (max_node + 1)
    parent = [None] * (max_node + 1)

    distance[start] = 0

    pq = PriorityQueue()
    pq.put((0, start))  # put (distance -> 0 to start node and node itself) as a tuple

    while not pq.empty():
        min_distance, node = pq.get()
        if node == target:
            break
        for edge in graph[node]:
            new_distance = min_distance + edge.weight
            if new_distance < distance[edge.destination]:
                distance[edge.destination] = new_distance
                parent[edge.destination] = node
                pq.put((new_distance, edge.destination))

    return distance, parent


def reconstruct_path(target, distance, parent):
    if distance[target] == float("inf"):
        return None, None

    path = deque()
    node = target
    while node is not None:
        path.appendleft(node)
        node = parent[node]

    return path, distance[target]


edges_count = int(input())
graph = construct_graph(edges_count)

start_node = int(input())
end_node = int(input())
distance, parent = dijkstra(start_node, end_node, graph)

path, path_length = reconstruct_path(end_node, distance, parent)

if not path:
    print("There is no such path.")
else:
    print(f"{path_length}\n"
          f"{' '.join(str(x) for x in path)}")
