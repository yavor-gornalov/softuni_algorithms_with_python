# https://judge.softuni.org/Contests/Practice/Index/3563#2

from collections import deque


def construct_visited(start_node, graph):
    visited = [False] * (len(graph))

    queue = deque([start_node])
    visited[start_node] = True

    while queue:
        node = queue.popleft()
        for child in graph[node]:
            if not visited[child]:
                visited[child] = True
                queue.append(child)

    return visited


nodes = int(input()) + 1
edges = int(input())

graph = []
[graph.append([]) for _ in range(nodes)]

for _ in range(edges):
    source, destination = [int(x) for x in input().split()]
    graph[source].append(destination)

start_node = int(input())

visited = construct_visited(start_node, graph)


def get_unreachable_nodes(visited):
    unreachable_nodes = []
    for node in range(1, len(visited)):
        if not visited[node]:
            unreachable_nodes.append(node)

    return unreachable_nodes


result = get_unreachable_nodes(visited)

print(*result, sep=" ")
