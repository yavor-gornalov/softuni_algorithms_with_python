# https://judge.softuni.org/Contests/Practice/Index/3465#2

class Edge:
    def __init__(self, first, second, cost):
        self.first = first
        self.second = second
        self.cost = cost

    def __gt__(self, other):
        return self.cost > other.cost


def find_root(parent, node):
    while node != parent[node]:
        node = parent[node]
    return node


def get_cheep_cost(graph):
    # Kruskal's algorithm used
    # forest = [] - for future use if path needed
    parent = [node for node in range(len(graph))]
    total_cost = 0
    for edge in sorted(graph):
        first_node_root = find_root(parent, edge.first)
        second_node_root = find_root(parent, edge.second)
        if first_node_root != second_node_root:
            parent[first_node_root] = second_node_root
            total_cost += edge.cost
            # forest.append(edge) - for future use if path needed
    return total_cost


nodes_count = int(input())
edges_count = int(input())

graph = []
for _ in range(edges_count):
    first, second, cost = [int(x) for x in input().split(" - ")]
    graph.append(Edge(first, second, cost))
    graph.append(Edge(second, first, cost))

total_cost = get_cheep_cost(graph)
print(f"Total cost: {total_cost}")
