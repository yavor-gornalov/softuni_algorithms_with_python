"""
Depth First Search (DFS)- Example
Used LIST for graph creation
"""


def dfs(graph, node, visited):
    if visited[node]:
        return

    visited[node] = True
    for child in graph[node]:
        dfs(graph, child, visited)

    print(node, end=" ")


# nodes from 0 to N continuously
graph = [
    [3, 6],  # N0
    [3, 6, 4, 2, 5],  # N1
    [1, 4, 5],  # N2
    [5, 0, 1],  # N3
    [1, 2, 6],  # N4
    [2, 1, 3],  # N5
    [0, 1, 4]  # N6
]

visited = [False] * len(graph)

for node in range(len(graph)):
    dfs(graph, node, visited)
