# https://judge.softuni.org/Contests/Practice/Index/3462#1
"""
Second version for topological sorting with cycle detection, DO NOT SUBMIT IN JUDGE (60/100)!
"""

from collections import deque


def top_sort_dfs(node, sorted_nodes, graph, visited, cycles):
    if node in cycles:
        raise Exception("Graph has cycles")
    if node in visited:
        return

    visited.add(node)
    cycles.add(node)

    for child in graph[node]:
        top_sort_dfs(child, sorted_nodes, graph, visited, cycles)

    cycles.remove(node)
    sorted_nodes.appendleft(node)


nodes = int(input())
graph = {}
for _ in range(nodes):
    node, children_str = input().split(" ->")
    children = [c.strip() for c in children_str.split(",")] if children_str else []
    graph[node] = children

visited = set()
cycles = set()
sorted_nodes = deque()
try:
    for node in graph:
        top_sort_dfs(node, sorted_nodes, graph, visited, cycles)
    print(f"Topological sorting: {', '.join([x for x in sorted_nodes])}")
except:
    print("Invalid topological sorting")
