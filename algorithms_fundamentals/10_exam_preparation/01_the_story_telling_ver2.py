# https://judge.softuni.org/Contests/Practice/Index/3474#0

from collections import deque


def construct_graph():
    graph = {}
    while True:
        line = input()
        if line == "End":
            break

        node, children = line.split(" ->")
        if node not in graph:
            graph[node] = [child.strip() for child in children.split()]
    return graph


def top_sort_dfs(node, graph, visited, cycle_nodes):
    if node in cycle_nodes:
        return "Error: cycle detected"

    if node not in visited:
        visited.add(node)
        cycle_nodes.add(node)

        for child in graph[node]:
            top_sort_dfs(child, graph, visited, cycle_nodes)

        cycle_nodes.remove(node)
        sorted_nodes.appendleft(node)


graph = construct_graph()

sorted_nodes = deque()  # linked list to hold the result
visited = set()  # set of already visited nodes
cycle_nodes = set()  # set of nodes in the current DFS cycle

for node in graph:
    top_sort_dfs(node, graph, visited, cycle_nodes)

print(*sorted_nodes)
