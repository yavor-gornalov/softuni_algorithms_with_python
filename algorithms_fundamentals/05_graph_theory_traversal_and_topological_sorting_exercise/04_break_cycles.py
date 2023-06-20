# https://judge.softuni.org/Contests/Practice/Index/3463#3


def dfs(node, destination, graph, visited):
    if node in visited:
        return

    visited.add(node)

    if node == destination:
        return

    for child in graph[node]:
        dfs(child, destination, graph, visited)


def path_exist(source, destination, graph):
    visited = set()

    dfs(source, destination, graph, visited)

    return destination in visited


nodes = int(input())

graph = {}
edges = []
for _ in range(nodes):
    node, children_str = input().split(" ->")
    graph[node] = []
    if not children_str:
        continue
    children = [x.strip() for x in children_str.split()]
    graph[node] = children
    for child in children:
        edges.append((node, child))

edges_to_remove = []
removed_edges_count = 0
for source, destination in sorted(edges, key=lambda x: (x[0], x[1])):
    if source not in graph[destination] or destination not in graph[source]:
        continue
    graph[source].remove(destination)
    graph[destination].remove(source)

    if path_exist(source, destination, graph):
        edges_to_remove.append((source, destination))
        removed_edges_count += 1
    else:
        graph[source].append(destination)
        graph[destination].append(source)

print(f"Edges to remove: {removed_edges_count}")
for source, destination in edges_to_remove:
    print(f"{source} - {destination}")
