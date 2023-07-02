# https://judge.softuni.org/Contests/Practice/Index/3623#2

from collections import deque


def construct_graph(nodes, edges):
    current_graph = []
    [current_graph.append([]) for _ in range(nodes + 1)]
    for _ in range(edges):
        source, destination = [int(x) for x in input().split()]
        current_graph[source].append(destination)
    return current_graph


def get_parents(current_graph, start_node, end_node):
    parent = [None] * (nodes_count + 1)
    visited = [False] * (nodes_count + 1)

    queue = deque([start_node])
    visited[start_node] = True

    while queue:
        node = queue.popleft()
        if node == end_node:
            continue
        for child in current_graph[node]:
            if not visited[child]:
                visited[child] = True
                queue.append(child)
                parent[child] = node

    return parent


def reconstruct_path(parent, end_node):
    current_path = deque()
    node = end_node

    while parent[node] is not None:
        current_path.appendleft(node)
        node = parent[node]
    current_path.appendleft(node)

    return current_path


nodes_count = int(input())
edges_count = int(input())

graph = construct_graph(nodes_count, edges_count)

start = int(input())
end = int(input())

prev = get_parents(graph, start, end)

path = reconstruct_path(prev, end)

if len(path) > 1:
    print(*path, sep=" ")
