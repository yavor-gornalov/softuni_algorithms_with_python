# https://judge.softuni.org/Contests/Practice/Index/3474#0

def get_graph_dependencies(graph):
    result = {}
    for node, children in graph.items():
        if node not in result:
            result[node] = 0
        for child in children:
            if child not in result:
                result[child] = 0
            result[child] += 1
    return result


def get_node_without_dependencies(graph_dependencies):
    node_to_remove = None
    for node in graph_dependencies:
        if graph_dependencies[node] == 0:
            node_to_remove = node
    return node_to_remove


graph = {}
while True:
    line = input()
    if line == "End":
        break

    node, children_str = line.split(" ->")
    if node not in graph:
        graph[node] = []
    for destination in children_str.strip().split():
        graph[node].append(destination)

graph_dependencies = get_graph_dependencies(graph)

has_cycles = False
sorted_nodes = []
while graph_dependencies:
    node_to_remove = get_node_without_dependencies(graph_dependencies)
    if node_to_remove is None:
        has_cycles = True
        break
    graph_dependencies.pop(node_to_remove)
    sorted_nodes.append(node_to_remove)
    for child in graph[node_to_remove]:
        graph_dependencies[child] -= 1

if not has_cycles:
    print(*sorted_nodes, sep=" ")
