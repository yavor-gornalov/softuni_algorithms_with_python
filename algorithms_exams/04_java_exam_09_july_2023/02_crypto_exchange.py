# https://judge.softuni.org/Contests/Practice/Index/4041#1
from collections import deque


def calculate_currency_swaps(start_node, target_node, current_graph):
    visited = set()
    parent = {start_node: None}

    queue = deque([start_node])
    visited.add(start_node)

    # BFS
    while queue:
        node = queue.popleft()
        if node == target_node:
            break
        for child in current_graph[node]:
            if child not in visited:
                visited.add(child)
                parent[child] = node
                queue.append(child)

    if target_node not in parent:
        return - 1

    path = []
    node = target_node
    while node is not None:
        path.append(node)
        node = parent[node]

    return len(path) - 1


edges_count = int(input())

graph = {}

for _ in range(edges_count):
    currency_from, currency_to = input().split(" - ")
    if currency_from not in graph:
        graph[currency_from] = []
    if currency_to not in graph:
        graph[currency_to] = []
    graph[currency_from].append(currency_to)
    graph[currency_to].append(currency_from)

source_currency, target_currency = input().split(" -> ")

result = calculate_currency_swaps(source_currency, target_currency, graph)

print(result)
