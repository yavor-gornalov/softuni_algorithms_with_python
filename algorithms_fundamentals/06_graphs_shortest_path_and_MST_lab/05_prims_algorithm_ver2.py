# https://judge.softuni.org/Contests/Practice/Index/3464#4
"""
Spanning Tree
    Subgraph without cycles (tree)
    Connects all vertices together
All connected graphs have a spanning tree
All graphs with multiple components have spanning forest

Prim's Algorithm
    Given a graph G(V, E) find the minimum spanning forest T(V', E')
    Attach to the tree T the starting node
    While smallest edge exists
        Attach to T the smallest possible edge from G without creating a cycle in T
            Use the smallest edge (u, v), such that u ∈ T and v ∉ T
Start the Prim's algorithm for each node from G

Prim's Algorithm (with Priority Queue)
spanningTreeNodes = Ø
foreach (v ϵ graphVertices)
    if (v ∉ spanningTreeNodes)
        prim(v)
prim(startNode)
    spanningTreeNodes -> startNode
    var priorityQueue = Ø
    priorityQueue -> childEdges(startNode)
    while (priorityQueue is not empty)
        smallestEdge = priorityQueue.ExtractMin()
        if (smallestEdge connects tree node with non-tree node)
            print smallestEdge
            spanningTreeNodes -> smallestEdge.nonTreeNode
            priorityQueue -> childEdges(smallestEdge.nonTreeNode
"""
from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight


def construct_graph(edges):
    graph = {}
    for _ in range(edges):
        first, second, weight = [int(x) for x in input().split(", ")]
        if first not in graph:
            graph[first] = []
        if second not in graph:
            graph[second] = []
        edge = Edge(first, second, weight)
        graph[first].append(edge)
        graph[second].append(edge)
    return graph


def prim(node, graph, forest, forest_edges):
    forest.add(node)
    pq = PriorityQueue()

    for edge in graph[node]:
        pq.put(edge)

    while not pq.empty():
        min_edge = pq.get()
        non_tree_node = -1

        if min_edge.first in forest and min_edge.second not in forest:
            non_tree_node = min_edge.second
        elif min_edge.first not in forest and min_edge.second in forest:
            non_tree_node = min_edge.first

        if non_tree_node == -1:
            continue

        forest.add(non_tree_node)
        forest_edges.append(min_edge)

        for edge in graph[non_tree_node]:
            pq.put(edge)


edges_count = int(input())
graph = construct_graph(edges_count)

forest = set()
forest_edges = []
for node in graph:
    if node in forest:
        continue
    prim(node, graph, forest, forest_edges)

for edge in forest_edges:
    print(f"{edge.first} - {edge.second}")
