# https://judge.softuni.org/Contests/Practice/Index/2481#2

"""
This is a problem from Algorithms with Java course.
Python to Java converter used for testing the code in judge system
"""


def dfs(node, graph, visited):
    if node in visited:
        return

    visited.add(node)
    for child in graph[node]:
        dfs(child, graph, visited)


nodes_count = int(input())
edges_count = int(input())

graph = []
[graph.append([]) for _ in range(nodes_count + 1)]

for _ in range(edges_count):
    source, destination = [int(x) for x in input().split()]
    graph[source].append(destination)

start_node = int(input())

visited = set()

dfs(start_node, graph, visited)

print(*[node for node in range(1, nodes_count + 1) if node not in visited], sep=" ")
