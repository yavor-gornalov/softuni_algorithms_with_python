# https://judge.softuni.org/Contests/Practice/Index/2484#2

from collections import deque


def construct_graph(nodes, edges):
    graph = []
    [graph.append([]) for _ in range(nodes + 1)]

    for _ in range(edges):
        source, destination = [int(x) for x in input().split()]
        graph[source].append(destination)

    return graph


def graph_shortest_path(start, target, graph):
    visited = [False] * len(graph)
    path = []

    visited[start] = True
    target_found = False
    queue = deque([start])
    # BFS
    while queue:
        node = queue.popleft()

        if not target_found:
            path.append(node)
            target_found = node == target

        for child in graph[node]:
            if not visited[child]:
                visited[child] = True
                queue.append(child)

    print(*path)
    print(*[idx for idx in range(1, len(visited)) if not visited[idx]])


def get_inaccessible_nodes(visited):
    inaccessible_nodes = []
    for node in range(1, len(visited)):
        if not visited[node]:
            inaccessible_nodes.append(node)

    return inaccessible_nodes


nodes_count = int(input())
edges_count = int(input())

current_graph = construct_graph(nodes_count, edges_count)

start_node = int(input())
target_node = int(input())

graph_shortest_path(start_node, target_node, current_graph)
