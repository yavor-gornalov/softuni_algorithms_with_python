# https://judge.softuni.org/Contests/Practice/Index/3474#2
from collections import deque
from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight


def construct_graph(nodes, edges):
    graph = []
    [graph.append([]) for _ in range(nodes)]
    for _ in range(edges):
        first, second, weight = [int(x) for x in input().split()]
        edge = Edge(first, second, weight)
        graph[first].append(edge)
        graph[second].append(edge)
    return graph


def prim(node, graph, forest):
    forest.add(node)
    pq = PriorityQueue()
    parent = [None] * len(graph)

    for edge in graph[node]:
        pq.put(edge)

    while not pq.empty():
        min_edge = pq.get()
        non_tree_node = -1
        tree_node = -1

        if min_edge.first in forest and min_edge.second not in forest:
            tree_node, non_tree_node = min_edge.first, min_edge.second
        elif min_edge.first not in forest and min_edge.second in forest:
            tree_node, non_tree_node = min_edge.second, min_edge.first

        if non_tree_node == -1:
            continue

        forest.add(non_tree_node)

        for edge in graph[non_tree_node]:
            pq.put(edge)
            parent[non_tree_node] = tree_node

    return parent


def damage_by_neighbourhood(parent, forest, strikes_by_node, power):
    for current_node in strikes_by_node:
        if current_node not in forest:
            continue
        counter = 0
        node = current_node
        while parent[node] is not None:
            node = parent[node]
            counter += 1
        strikes_by_node[current_node] += power // 2 ** counter
    return strikes_by_node


neighbourhoods_count = int(input())
neighbourhood_connections = int(input())
lighting_strikes_count = int(input())

city_graph = construct_graph(neighbourhoods_count, neighbourhood_connections)

lighting_strikes_by_neighbourhood = dict.fromkeys(range(neighbourhoods_count), 0)

for _ in range(lighting_strikes_count):
    current_struck_neighbourhoods = set()  # forest
    struck_neighbourhood, lighting_power = [int(x) for x in input().split()]
    lighting_parent = prim(struck_neighbourhood, city_graph, current_struck_neighbourhoods)
    lighting_strikes_by_neighbourhood = damage_by_neighbourhood(lighting_parent,
                                                                current_struck_neighbourhoods,
                                                                lighting_strikes_by_neighbourhood,
                                                                lighting_power)

print(max(lighting_strikes_by_neighbourhood.values()))
