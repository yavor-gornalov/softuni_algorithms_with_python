def dfs(node, graph, visited):
    if visited[node]:
        return
    visited[node] = True
    for child in graph[node]:
        dfs(child, graph, visited)


nodes_count = int(input())
edges_count = int(input())

graph = []
[graph.append([]) for _ in range(nodes_count)]

edges = set()
for _ in range(edges_count):
    source, destination = [int(x) for x in input().split(" - ")]
    graph[source].append(destination)
    graph[destination].append(source)
    edges.add((min(source, destination), max(source, destination)))

important_streets = []

for source, destination in edges:
    graph[source].remove(destination)
    graph[destination].remove(source)

    visited = [False] * nodes_count
    dfs(0, graph, visited)

    if not all(visited):
        important_streets.append((source, destination))

    graph[source].append(destination)
    graph[destination].append(source)

print("Important streets:")
for source, destination in important_streets:
    print(source, destination, sep=" ")
