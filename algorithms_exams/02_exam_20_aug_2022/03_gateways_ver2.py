# https://judge.softuni.org/Contests/Practice/Index/3623#2
from collections import deque


def construct_graph(nodes, edges):
    current_graph = []
    [current_graph.append([]) for _ in range(nodes + 1)]

    for _ in range(edges):
        source, destination = [int(x) for x in input().split()]
        current_graph[source].append(destination)
    return current_graph


def find_parent(start, end, graph):
    visited = [False] * len(graph)
    parent = [None] * len(graph)
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        if node == end:
            continue
        for child in graph[node]:
            if not visited[child]:
                visited[child] = True
                parent[child] = node
                queue.append(child)
    return parent


def reconstruct_path(target, parent):
    path = deque()
    node = target
    while parent[node] is not None:
        path.appendleft(node)
        node = parent[node]
    path.appendleft(node)
    return path


nodes_count = int(input())
edges_count = int(input())
current_graph = construct_graph(nodes_count, edges_count)

start_node = int(input())
end_node = int(input())

parent = find_parent(start_node, end_node, current_graph)
path = reconstruct_path(end_node, parent)

if len(path) > 1:
    print(*path)
