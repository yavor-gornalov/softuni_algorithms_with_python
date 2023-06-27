# https://judge.softuni.org/Contests/Practice/Index/3465#0

from collections import deque


def shortest_path(start_node, end_node, graph):
    queue = deque([start_node])
    visited = {start_node}
    parent = {end_node: None}

    while queue:
        node = queue.popleft()
        if node == end_node:
            break
        for child in graph[node]:
            if child not in visited:
                visited.add(child)
                queue.append(child)
                parent[child] = node

    if parent[end_node] is None:
        return -1
    else:
        result = 0
        if parent[end_node] is not None:
            node = end_node
            while node in parent:
                node = parent[node]
                result += 1

    return result


nodes_count = int(input())
number_of_pairs = int(input())

graph = {}
for _ in range(nodes_count):
    node, edges_str = input().split(":")
    graph[node] = edges_str.split() if edges_str else []

for _ in range(number_of_pairs):
    first, second = input().split("-")
    path_length = shortest_path(first, second, graph)
    print(f"{{{first}, {second}}} -> {path_length}")
