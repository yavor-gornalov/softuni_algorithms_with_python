# https://judge.softuni.org/Contests/Practice/Index/3462#1

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
    for node in graph_dependencies:
        if graph_dependencies[node] == 0:
            return node
    return None


nodes = int(input())

graph = {}
for _ in range(nodes):
    node, children_str = input().split(" ->")
    children = [c.strip() for c in children_str.split(",")] if children_str else []
    graph[node] = children

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

if has_cycles:
    print("Invalid topological sorting")
else:
    print(f"Topological sorting: {', '.join([x for x in sorted_nodes])}")
