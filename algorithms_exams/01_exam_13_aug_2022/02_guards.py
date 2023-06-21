# https://judge.softuni.org/Contests/Practice/Index/3592#1

def dfs(node, graph, visited):
    if visited[node]:
        return
    visited[node] = True
    for child in graph[node]:
        dfs(child, graph, visited)


nodes_count = int(input())
edges_count = int(input())

graph = []
[graph.append([]) for _ in range(nodes_count + 1)]

edges = []
for _ in range(edges_count):
    source, destination = [int(x) for x in input().split()]
    graph[source].append(destination)

    edges.append((source, destination))
starting_node = int(input())

visited = [False] * (nodes_count + 1)

dfs(starting_node, graph, visited)

print(*[x for x in range(len(visited)) if x != 0 and not visited[x]])
