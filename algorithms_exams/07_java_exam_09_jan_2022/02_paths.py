# # https://judge.softuni.org/Contests/Practice/Index/3346#0

def dfs(node, target, graph, visited, path):
    visited[node] = True
    path.append(node)

    if node == target:
        print(*path, sep=" ")
    else:
        for child in graph[node]:
            if visited[child]:
                continue
            dfs(child, target, graph, visited, path)
    path.pop()
    visited[node] = False


nodes = int(input())
graph = []
[graph.append([]) for _ in range(nodes)]
for node in range(nodes):
    children = [int(x) for x in input().split()]
    graph[node] = children if children else []

for start_node in range(nodes - 1):
    visited = [False] * nodes
    path = []
    dfs(start_node, nodes - 1, graph, visited, path)
