"""
Depth First Search (DFS) - Example
Used DICTIONARY for graph creation
"""


def dfs(graph, node, visited):
    if node in visited:
        return

    visited.add(node)
    for child in graph[node]:
        dfs(graph, child, visited)

    print(node, end=" ")


graph = {
    7: [19, 21, 14],
    19: [1, 12, 31, 21],
    1: [7],
    12: [],
    31: [21],
    21: [14],
    14: [23, 6],
    6: [],
    23: [21],
}

visited = set()

for node in graph:
    dfs(graph, node, visited)
