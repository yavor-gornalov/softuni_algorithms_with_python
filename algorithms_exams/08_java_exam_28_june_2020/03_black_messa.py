# https://judge.softuni.org/Contests/Practice/Index/2484#2

from collections import deque


def construct_graph(nodes, edges):
    graph = [[0] * (nodes + 1) for _ in range(nodes + 1)]
    for _ in range(edges):
        source, destination = [int(x) for x in input().split()]
        graph[source][destination] = 1

    return graph


def graph_shortest_path(start, target, graph):
    visited = [False] * len(graph)
    path = []

    target_found = False
    queue = deque([start])
    # BFS
    while queue:
        node = queue.popleft()
        visited[node] = True

        if not target_found:
            path.append(node)
            target_found = node == target

        for child in range(len(graph[node])):
            if graph[node][child] != 0 and not visited[child]:
                visited[child] = True
                queue.append(child)

    print(*path)
    print(*[idx for idx in range(1, len(visited)) if not visited[idx]])


nodes_count = int(input())
edges_count = int(input())

current_graph = construct_graph(nodes_count, edges_count)

start_node = int(input())
target_node = int(input())

graph_shortest_path(start_node, target_node, current_graph)
