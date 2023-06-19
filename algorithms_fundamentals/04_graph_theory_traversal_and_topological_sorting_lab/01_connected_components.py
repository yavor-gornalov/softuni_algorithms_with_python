# https://judge.softuni.org/Contests/Practice/Index/3462#0

def dfs(node, graph, visited, path):
    if visited[node]:
        return

    visited[node] = True
    for child in graph[node]:
        dfs(child, graph, visited, path)
    path.append(node)


nodes = int(input())

graph = []
for _ in range(nodes):
    current_node = [int(x) for x in input().split()]
    graph.append(current_node)

visited = [False] * nodes
for node in range(len(graph)):
    if visited[node]:
        continue
    path = []
    dfs(node, graph, visited, path)
    print(f"Connected component: {' '.join([str(p) for p in path])}")
