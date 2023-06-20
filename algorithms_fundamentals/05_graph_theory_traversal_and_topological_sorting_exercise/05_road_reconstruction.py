# https://judge.softuni.org/Contests/Practice/Index/3463#4

def dfs(node, graph, visited):
    if node in visited:
        return

    visited.add(node)
    for child in graph[node]:
        dfs(child, graph, visited)


def all_nodes_accessible(graph):
    visited = set()

    dfs(0, graph, visited)

    return len(visited) == nodes_count


nodes_count = int(input())
edges_count = int(input())

graph = [None] * nodes_count
edges = []
for node in range(edges_count):
    source, destination = [int(x) for x in input().split(" - ")]
    if graph[source] is None:
        graph[source] = []
    if graph[destination] is None:
        graph[destination] = []
    graph[source].append(destination)
    graph[destination].append(source)

    edges.append((min(source, destination), max(source, destination)))

important_streets = []
for source, destination in edges:
    graph[source].remove(destination)
    graph[destination].remove(source)

    if not all_nodes_accessible(graph):
        important_streets.append((source, destination))

    graph[source].append(destination)
    graph[destination].append(source)

print("Important streets:")
for source, destination in important_streets:
    print(source, destination, sep=" ")
