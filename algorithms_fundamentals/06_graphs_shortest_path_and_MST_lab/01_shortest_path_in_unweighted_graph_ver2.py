# https://judge.softuni.org/Contests/Compete/Index/3464#0

"""
In unweighted graphs finding the shortest path can be done
with BFS

bfs(G, start, end)
    visited[start] = true
    queue.enqueue(start)
    while (!queue.isEmpty())
        v = queue.dequeue()
        if v is end
        return v
        for all edges from v to w in G.adjacentEdges(v) do
            if w is not labeled as discovered then
                label w as discovered
                w.parent = v
                queue.enqueue(w)
"""

from collections import deque


def construct_graph(nodes, edges):
    graph = []
    [graph.append([]) for _ in range(nodes + 1)]

    for _ in range(edges):
        source, destination = [int(x) for x in input().split()]
        graph[source].append(destination)

    return graph


def get_parent_bfs(start, end, graph):
    size = len(graph)
    visited = [False] * size
    parent = [None] * size

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


def reconstruct_path(target, graph):
    path = deque()
    node = end_node
    while node is not None:
        path.appendleft(node)
        node = parent[node]
    return path


def print_results(path):
    print(f"Shortest path length is: {len(path) - 1}\n"
          f"{' '.join(str(x) for x in path)}")


nodes_count = int(input())
edges_count = int(input())
current_graph = construct_graph(nodes_count, edges_count)

start_node = int(input())
end_node = int(input())
parent = get_parent_bfs(start_node, end_node, current_graph)
current_path = reconstruct_path(end_node, current_graph)

print_results(current_path)
