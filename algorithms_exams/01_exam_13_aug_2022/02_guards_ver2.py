# https://judge.softuni.org/Contests/Practice/Index/3592#1

def dfs(node, graph, unvisited):
    if node not in unvisited:
        return
    unvisited.remove(node)
    for child in graph[node]:
        dfs(child, graph, unvisited)


nodes_count = int(input())
edges_count = int(input())

graph = {node: [] for node in range(1, nodes_count + 1)}

for _ in range(edges_count):
    source, destination = [int(x) for x in input().split()]
    graph[source].append(destination)

starting_node = int(input())

unvisited = list(graph.keys())
dfs(starting_node, graph, unvisited)

print(*unvisited)
