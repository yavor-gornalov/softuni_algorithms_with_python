# https://judge.softuni.org/Contests/Practice/Index/4004#1

"""
This is a problem from Algorithms with Java course.
Python to Java converter used for testing the code in judge system
"""

from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, amount):
        self.first = first
        self.second = second
        self.amount = amount

    def __gt__(self, other):
        return self.amount > other.amount


def prim(node, graph, forest):
    if node in forest:
        return 0

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

        for edge in graph[non_tree_node]:
            pq.put(edge)

    return 1


edges = int(input())

graph = {}

for _ in range(edges):
    first, second, amount = input().split()
    edge = Edge(first, second, int(amount))
    if first not in graph:
        graph[first] = []
    if second not in graph:
        graph[second] = []
    graph[first].append(edge)
    graph[second].append(edge)

forest = set()
total_trees_in_forest = 0
for node in graph:
    total_trees_in_forest += prim(node, graph, forest)

print(total_trees_in_forest)
