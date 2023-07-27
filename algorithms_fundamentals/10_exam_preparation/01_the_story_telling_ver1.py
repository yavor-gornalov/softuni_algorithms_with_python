# https://judge.softuni.org/Contests/Practice/Index/3474#0

def construct_graph():
    graph = {}
    while True:
        line = input()
        if line == "End":
            break

        node, children = line.split(" ->")
        if node not in graph:
            graph[node] = [child.strip() for child in children.split()]
    return graph


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
    node_without_dependencies = None
    for node in graph_dependencies:
        if graph_dependencies[node] == 0:
            node_without_dependencies = node
    return node_without_dependencies


def sort_graph_by_source_removal(graph):
    sorted_nodes = []
    while graph_dependencies:
        node_to_remove = get_node_without_dependencies(graph_dependencies)
        if node_to_remove is None:
            break
        graph_dependencies.pop(node_to_remove)
        sorted_nodes.append(node_to_remove)
        for child in graph[node_to_remove]:
            graph_dependencies[child] -= 1
    return sorted_nodes


graph = construct_graph()
graph_dependencies = get_graph_dependencies(graph)
result = sort_graph_by_source_removal(graph)

print(*result)
