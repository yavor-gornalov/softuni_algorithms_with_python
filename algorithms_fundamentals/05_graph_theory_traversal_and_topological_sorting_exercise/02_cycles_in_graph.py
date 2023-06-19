# https://judge.softuni.org/Contests/Practice/Index/3463#1

def top_sort_dfs(node, graph, visited, cycles):
    if node in cycles:
        raise Exception
    if node in visited:
        return

    visited.add(node)
    cycles.add(node)

    for child in graph[node]:
        top_sort_dfs(child, graph, visited, cycles)

    cycles.remove(node)


graph = {}
while True:
    line = input()
    if line == "End":
        break
    source, destination = line.split("-")
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(destination)

visited = set()
cycles = set()

try:
    for node in graph:
        top_sort_dfs(node, graph, visited, cycles)
    print("Acyclic: Yes")
except:
    print("Acyclic: No")
