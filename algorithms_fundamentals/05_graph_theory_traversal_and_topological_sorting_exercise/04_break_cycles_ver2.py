# https://judge.softuni.org/Contests/Practice/Index/3463#3

def get_visited_nodes(node, target, visited, graph):
    if node in visited:
        return

    visited.add(node)

    if node == target:
        return

    for child in graph[node]:
        get_visited_nodes(child, target, visited, graph)


nodes_count = int(input())

graph = {}
edges = []
for _ in range(nodes_count):
    line = input()
    node, children_str = line.split(" ->")

    graph[node] = []
    if not children_str:
        continue
    children = children_str.strip().split()
    for child in children:
        graph[node].append(child)
        edges.append((node, child))

removed_edges_count = 0
removed_edges = []
for (source, destination) in sorted(edges):
    if destination not in graph[source] or source not in graph[destination]:
        continue

    graph[source].remove(destination)
    graph[destination].remove(source)

    visited = set()
    get_visited_nodes(source, destination, visited, graph)
    if destination in visited:
        removed_edges_count += 1
        removed_edges.append((source, destination))
        continue

    graph[source].append(destination)
    graph[destination].append(source)

print(f"Edges to remove: {removed_edges_count}")
[print(f"{src} - {dst}") for (src, dst) in removed_edges]
