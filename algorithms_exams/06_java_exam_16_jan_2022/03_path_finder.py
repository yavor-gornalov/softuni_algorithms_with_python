# https://judge.softuni.org/Contests/Practice/Index/3347#2

def path_finder(path, graph):
    path_exists = True
    for idx in range(1, len(path)):
        current_parent = path[idx - 1]
        current_child = path[idx]
        if current_child not in graph[current_parent]:
            path_exists = False
            break
    return path_exists


nodes = int(input())

graph = []
[graph.append([]) for _ in range(nodes)]
for node in range(nodes):
    children = [int(x) for x in input().split()]
    if children:
        graph[node] = children

paths_count = int(input())
possible_paths = []
[possible_paths.append([]) for _ in range(paths_count)]
for path_number in range(paths_count):
    possible_paths[path_number] = [int(x) for x in input().split()]

for current_path in possible_paths:
    is_path_possible = (path_finder(current_path, graph))
    print("yes") if is_path_possible else print("no")
