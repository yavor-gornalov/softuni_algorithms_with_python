# https://judge.softuni.org/Contests/Practice/Index/3465#0

from collections import deque


def shortest_path(start_node, end_node, graph):
    visited = [False] * len(graph)
    parent = [None] * len(graph)

    queue = deque([start_node])
    visited[start_node] = True

    while queue:
        node = queue.popleft()
        if node == end_node:
            break
        for child in graph[node]:
            if not visited[child]:
                visited[child] = True
                queue.append(child)
                parent[child] = node

    result = -1
    if parent[end_node] is not None:
        node = end_node
        while node is not None:
            node = parent[node]
            result += 1

    return result


nodes_count = int(input())
number_of_pairs = int(input())

graph = []
[graph.append([]) for _ in range(nodes_count + 1)]
for _ in range(1, nodes_count + 1):
    node, edges_str = input().split(":")
    node = int(node)
    graph[node] = [int(e) for e in edges_str.split()] if edges_str else []

for _ in range(number_of_pairs):
    first, second = [int(x) for x in input().split("-")]
    path_length = shortest_path(first, second, graph)
    print(f"{{{first}, {second}}} -> {path_length}")
