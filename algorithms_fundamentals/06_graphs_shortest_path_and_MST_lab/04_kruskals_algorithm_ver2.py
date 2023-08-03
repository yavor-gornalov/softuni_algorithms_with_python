# https://judge.softuni.org/Contests/Practice/Index/3464#3
"""
Spanning Tree
    Subgraph without cycles (tree)
    Connects all vertices together
All connected graphs have a spanning tree
All graphs with multiple components have spanning forest

Kruskal's Algorithm:
Create a forest F holding all graph vertices and no edges
Create a set S holding all edges in the graph
While S is non-empty
    Remove the edge e with min weight
    If e connects two different trees
        Add e to the forest
        Join these two trees into a single tree
The graph may not be connected!

Kruskal's Algorithm – Pseudo Code:
foreach v ∈ graph edges
    parent[v] = v
foreach edge {u, v} ordered by weight(u, v)
    rootU = findRoot(u)
    rootV = findRoot(v)
    if rootU ≠ rootV
        print edge {u, v}
        parent[rootU] = rootV
findRoot(node)
    while (parent[node] ≠ node)
        node = parent[node]
    return node
"""


class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight


def find_root(parent, node):
    while node != parent[node]:
        node = parent[node]
    return node


def construct_graph(edges):
    max_node = float("-inf")
    graph = []
    for _ in range(edges):
        first, second, weight = [int(x) for x in input().split(", ")]
        graph.append(Edge(first, second, weight))
        max_node = max(first, second)
    return graph, max_node


def kruskal(graph, max_node):
    parent = [x for x in range(max_node + 1)]
    forest_edges = []
    for edge in sorted(graph, key=lambda e: e.weight):
        first_node_root = find_root(parent, edge.first)
        second_node_root = find_root(parent, edge.second)
        if first_node_root != second_node_root:
            parent[first_node_root] = second_node_root
            forest_edges.append(edge)
    return forest_edges


edges_count = int(input())
graph, max_node = construct_graph(edges_count)

forest_edges = kruskal(graph, max_node)

for edge in forest_edges:
    print(f"{edge.first} - {edge.second}")
