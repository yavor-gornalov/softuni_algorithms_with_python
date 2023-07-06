# https://judge.softuni.org/Contests/Practice/Index/3474#2

from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight


def calc_damage(jumps, damage):
    for _ in range(jumps):
        damage //= 2
    return damage


def prim(node, graph, damage, damage_by_node):
    jumps = [0] * len(graph)
    damage_by_node[node] += damage

    tree = {node}
    pq = PriorityQueue()

    for edge in graph[node]:
        pq.put(edge)

    while not pq.empty():
        min_edge = pq.get()
        tree_node, non_tree_node = -1, -1

        if min_edge.first in tree and min_edge.second not in tree:
            tree_node, non_tree_node = min_edge.first, min_edge.second
        elif min_edge.first not in tree and min_edge.second in tree:
            tree_node, non_tree_node = min_edge.second, min_edge.first

        if non_tree_node == -1:
            continue

        tree.add(non_tree_node)
        for edge in graph[non_tree_node]:
            pq.put(edge)

        jumps[non_tree_node] = jumps[tree_node] + 1
        damage_by_node[non_tree_node] += calc_damage(jumps[non_tree_node], damage)


nodes_count = int(input())
edges_count = int(input())
lightnings_count = int(input())

graph = {node: [] for node in range(nodes_count)}
for _ in range(edges_count):
    first, second, weight = [int(x) for x in input().split()]
    edge = Edge(first, second, weight)
    graph[first].append(edge)
    graph[second].append(edge)

damage_by_node = [0] * nodes_count
for _ in range(lightnings_count):
    node, damage = [int(x) for x in input().split()]

    prim(node, graph, damage, damage_by_node)

print(max(damage_by_node))
